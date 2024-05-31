import pandas as pd
from threading import Thread, Event
from datetime import datetime
import time
import os

class CSVMonitor(Thread):
    def __init__(self, root_dir, start_time, end_time, interval=10):
        super().__init__()
        self.root_dir = root_dir
        self.start_time = datetime.strptime(start_time, "%H:%M").time()
        self.end_time = datetime.strptime(end_time, "%H:%M").time()
        self.interval = interval
        self.is_active = Event()
        self.is_active.set()
        self.last_file = self.get_last_modified_file()
        self.last_checked = os.path.getmtime(self.last_file) if self.last_file else 0
        self.total_count = self.get_initial_count()
        self.new_pieces = 0

    def get_last_modified_file(self):
        current_month = datetime.now().strftime("%Y-%m")
        month_dir = os.path.join(self.root_dir, current_month)
        daily_dir = os.path.join(month_dir, "Daily")
        files = [os.path.join(daily_dir, f) for f in os.listdir(daily_dir) if f.endswith(".csv")]
        if files:
            return max(files, key=os.path.getmtime)
        return None

    def get_initial_count(self):
        if self.last_file:
            try:
                data = pd.read_csv(self.last_file)
                data['Date'] = pd.to_datetime(data['Date'])
                data = data[(data['Date'].dt.time >= self.start_time) & (data['Date'].dt.time <= self.end_time)]
                data = self.clean_data(data)
                passed = data[
                    (data['Result'] == 'PASS') &
                    (data['Continuity'] == 'PASS') &
                    (data['LooseContact'] == 'PASS') &
                    (data['WithstandVolt'] == 'PASS') &
                    (data['Insulation'] == 'PASS') &
                    (data['Continuity.1'] == 'PASS')
                ]
                return passed.shape[0]
            except Exception as e:
                print(f"Error al leer el archivo inicial: {e}")
                return 0
        return 0

    def clean_data(self, df):
        for col in df.select_dtypes(include=[object]).columns:
            df[col] = df[col].map(lambda x: x.strip() if isinstance(x, str) else x)
        return df

    # def run(self):
    #     while self.is_active.is_set():
    #         current_time = datetime.now().time()
    #         if self.start_time <= current_time <= self.end_time:
    #             current_file = self.get_last_modified_file()
    #             if current_file and os.path.getmtime(current_file) > self.last_checked:
    #                 self.last_file = current_file
    #                 self.last_checked = os.path.getmtime(current_file)
    #                 data = pd.read_csv(current_file)
    #                 data['Date'] = pd.to_datetime(data['Date'])
    #                 data = data[(data['Date'].dt.time >= self.start_time) & (data['Date'].dt.time <= self.end_time)]
    #                 data = self.clean_data(data)
    #                 passed = data[
    #                     (data['Result'] == 'PASS') &
    #                     (data['Continuity'] == 'PASS') &
    #                     (data['LooseContact'] == 'PASS') &
    #                     (data['WithstandVolt'] == 'PASS') &
    #                     (data['Insulation'] == 'PASS') &
    #                     (data['Continuity.1'] == 'PASS')
    #                 ]
    #                 new_count = passed.shape[0]
    #                 self.new_pieces = new_count - self.total_count
    #                 if self.new_pieces > 0:
    #                     self.total_count = new_count
    #                     print(f"Fecha: {datetime.now()}:   Piezas pasadas en el intervalo: {self.new_pieces}.   Total acumulado: {self.total_count}")
    #         time.sleep(self.interval)
    def get_data(self):
        current_file = self.get_last_modified_file()
        if not current_file:
            return pd.DataFrame(), 0 

        data = pd.read_csv(current_file)
        data['Date'] = pd.to_datetime(data['Date'])

        station_name = data['Name'].unique()[0]
        order_number = data['Order'].unique()[0]
        lot_number = data['Lot Number'].unique()[0]
       

        data = data[(data['Date'].dt.time >= self.start_time) & (data['Date'].dt.time <= self.end_time)]

      
        data = self.clean_data(data)

    
        passed = data[
            (data['Result'] == 'PASS') &
            (data['Continuity'] == 'PASS') &
            (data['LooseContact'] == 'PASS') &
            (data['WithstandVolt'] == 'PASS') &
            (data['Insulation'] == 'PASS') &
            (data['Continuity.1'] == 'PASS')
        ]
       

        new_count = passed.shape[0]
        non_passed_count = data.shape[0] - new_count
        return data, new_count, non_passed_count, station_name,order_number, lot_number



