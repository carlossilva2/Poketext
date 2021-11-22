import sqlite3
from sqlite3 import Error
import json
from hashlib import md5
from time import time


class PokeDB:

    def __init__(self, db_name: str) -> None:
        try:
            self.db = sqlite3.connect(f"{db_name}.db")
        except Error as e:
            print(e)

    def close_db(self):
        try:
            self.db.close()
        except Error:
            print(Error)
        
    def insert(self, data: dict, table: str, fields: list=None, empty: bool=False) -> str:
        return self.__insert(data, table, fields, empty)
    
    def get(self, name: str, table: str, json: bool=False) -> 'list[tuple]':
        cursor = self.db.cursor()
        cursor.execute(f"SELECT * FROM {table} WHERE name=?",(name,))
        ans = cursor.fetchall()
        return self.__to_json(ans, table) if json else ans

    def get_fields(self, table: str, fields: 'list[str]'=['*'], filter: 'list[tuple]'=None, json: bool=False) -> list:
        if type(fields) != list or table == "" or table == None:
            return []
        if fields == [] or fields == None:
            fields = ['*']
        cursor = self.db.cursor()
        s = "WHERE "
        values = []
        if filter != None and type(filter) == list:
            for f in filter:
                values.append(f[2])
                s = f"{s}{f[0]}{f[1]}? {f[3] if len(f)>3 else ''} "
        cursor.execute(f"SELECT {','.join(fields)} FROM {table} {'' if filter == None else s}",tuple(values))
        _ = cursor.fetchall()
        return _ if not json else self.__to_json(_, table, fields if "*" not in fields else None)

    def __insert(self, data: 'dict|tuple', table: str, spec_fields: list=None, empty: bool=False) -> str:
        if type(data) not in [list, tuple]:
            print("Type not supported")
            exit(1)
        temp = None
        if type(data) == dict:
            temp = json.dumps(data)
        else:
            temp = "".join([str(_) for _ in data])
        _id = self.__create_id(temp)
        if type(data) == tuple:
            d = list(data)
            d.insert(0,_id)
            temp = tuple(d)
        obj = self.__build_payload(data, _id) if type(data) == dict else temp
        cursor = self.db.cursor()
        columns = self.__get_columns(table) if spec_fields == None or spec_fields == [] else spec_fields
        if len(obj) != len(columns) and not empty:
            print("Payload size incomplete")
            exit(1)
        cursor.execute(f"INSERT INTO {table}{'(' if not empty else ''}{','.join(columns if not empty else [])}{')' if not empty else ''} VALUES({','.join(['?' for _ in range(len(columns))])})", obj)
        self.db.commit()
        return _id
    
    def __to_json(self, data: tuple, table: str, display: list=None) -> dict:
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM FieldMapping WHERE table_name=?",(table,))
        ans = cursor.fetchall()
        res = []
        for ele in data:
            obj = {}
            col = self.__get_columns(table, display)
            for k in col:
                for _ in ans:
                    if _[2] == k:
                        obj[_[3]] = None
                """ if len(ans) == 0:
                    obj[k] = None """
            for index,key in enumerate(obj.keys()):
                d = ele[index]
                if type(d) == str and (d.startswith("[") or d.startswith("{")):
                    obj[key] = json.loads(d)
                else:
                    obj[key] = d
            res.append(obj)
        return res if len(res) > 1 else res[0]
    
    def __build_payload(self, data: dict, _id: str="") -> tuple:
        obj = [_id if _id != "" or _id != None else None]
        for key in data.keys():
            obj.append(data[key] if type(data[key]) not in [list,dict] else json.dumps(data[key]))
        return tuple(obj)
    
    def __create_id(self, data: str) -> str:
        def encrypt(*args,**kwargs):
            "Method to encrypt data"
            if 'method' not in kwargs:
                raise AttributeError("You must specify a method to encrypt")
            try:
                method = eval(kwargs['method'])
            except Exception:
                exit(1)
            string = ""
            for item in args:
                string += str(item)
            return method(string.encode("UTF-8")).hexdigest()
        return encrypt(time(),data, method="md5")
    
    def __get_columns(self, table: str, display: list=None) -> list:
        if display == None:
            cursor = self.db.cursor()
            cursor.execute(f"PRAGMA table_info({table})")
            ans = [f[1] for f in cursor.fetchall()]
        else:
            ans = display
        return ans
    