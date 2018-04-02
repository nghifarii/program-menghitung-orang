class MesinKopi:
  name = ""
  beans = 0
  water = 0
  total_kopi = 0
  
  def __init__(self, name, beans, water):
      self.name = name
      self.beans = beans
      self.water = water
      MesinKopi.total_kopi += 1
      
      #Menambahkan kopi 
      #metode dengan argument tapi tidak bersifat mengembalikan/return
      def addBean(self, up):
          self.beans += up
      
      #Metode dengan return 
      def getBeans(self):
          return self.beans
      
      def removeBean(self):
          self.beans = self.beans - 1
       
      def addWater(self, up):
          self.water += up
      
      def minWater(self):
          return self.water
          
      def removeWater(self, down):
          self.water -= down
          
      def printState(self):
          print ("Name = " + self.name)
          print ("Beans = " + str(self.beans))
          print ("Water = " + str(self.water))
 
print ("=======Menu Default ===========")
bean = MesinKopi("Kopi Hitam", 80, 40)
bean = printState()
bean.addBean(10)
bean.removeWater(5)
print ("Kopi telah ditambah menjadi sebanyak %s " % + bean.getBean())
print ("Air telah dikurangi menjadi sebanyak %s " % + bean.minWater())
print ("==============Sekarang Menjadi=============")

nean.printState()
print ("Total kopi yang dipesan = ", MesinKopi.total_kopi)
