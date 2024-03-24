class Car: #車のクラスを作成しました。
  def __init__(self,speed,weight,car_type,tire_condition):
    self.speed = speed
    self.weight = weight
    self.car_type = car_type
    self.tire_condition = tire_condition
    
  def driving(self):
    print("運転中です。")
  
  def parking(self):
    print("駐車しています。")
    
  def maintenance(self):
    print("整備しています。")
    
car_A = Car(120,"3.5トン","プリウス","Perfect")
print(f'車Aのタイヤの状態は{car_A.tire_condition}です。')

car_B = Car(100,"4.5トン","N-BOX","Normal")
car_B.maintenance()

car_C = Car(180,"5トン","カローラ","Perfect")
print(f'車Cの車種は{car_C.car_type}です。')

car_D = Car(200, "6トン","BOXY","")