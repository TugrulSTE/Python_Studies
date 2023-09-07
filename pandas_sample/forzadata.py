import pandas as pd
import matplotlib.pyplot as plt

class FilterForza():
    def __init__(self):
        global pl_Info
        self.pl_Info=pd.read_excel("Forza_Horizon_Cars.xlsx",header=0)
        self.pl_Info["In_Game_Price"] = self.pl_Info["In_Game_Price"].fillna(0).astype(str).str.replace(",", "").astype(int)
        print(self.pl_Info["Model_type"].unique())
        
    def see_typesofcars(self):
        print(self.pl_Info["Model_type"].unique())
    
    def graph_models(self):
        model=list(self.pl_Info["Model_type"].unique())
        print(model)
        chc=int(input())
        chc-=1
        all_results=(self.pl_Info[self.pl_Info["Model_type"].str.contains(model[chc])])
        all_results=all_results.head(5)
        price=all_results["In_Game_Price"]
        brand=all_results["Name_and_model"]
        _,axs=plt.subplots()
        axs.plot(brand,price,"b")
        axs.set_xlabel("Models")
        axs.set_ylabel("Prices")
        plt.show()
        
    def modelType(self):
        model=input("Type of Car:")
        model=model.upper()
        all_results=(self.pl_Info[self.pl_Info["Model_type"].str.contains(model)])
        print(all_results[["Name_and_model","Model_type","In_Game_Price"]])
    
    def priceCar(self):
        max=int(input("Max. Price: "))
        min=int(input("Min. Price: "))
        for _, row in self.pl_Info.iterrows():
            price = row["In_Game_Price"]
            if price < max and price > min:
                print(row["Name_and_model"],row["In_Game_Price"])
                
    def price_model(self):
        model=input("Type of Car:")
        model=model.upper()
        max=int(input("Max. Price: "))
        min=int(input("Min. Price: "))
        all_results = self.pl_Info[self.pl_Info["Model_type"].str.contains(model)]
        
        for _, row in all_results.iterrows():
            price = row["In_Game_Price"]
            if price < max and price > min:
                print(row["Name_and_model"])

    def year_of_cars(self):
        min_year=int(input("Min. Year: "))
        max_year=int(input("Max. Year: "))
        for name in self.pl_Info["Name_and_model"]:
            if int(name[0:4])<max_year and int(name[0:4])>min_year:
                print(name)
                
    def expensive(self):
        self.pl_Info=self.pl_Info.sort_values("In_Game_Price",ascending=False)
        print (self.pl_Info.head(10)[["Name_and_model","In_Game_Price"]])
        
    def speed(self):
        self.pl_Info=self.pl_Info.sort_values("speed",ascending=False)
        print (self.pl_Info.head(10)[["Name_and_model","speed"]]) 
        
forza=FilterForza()

while True:
    choice=int(input("Welcome to ForzaFilter! \n Press 1- Filtering by Model Type \n 2- Filtering by Price Range \n 3- Filtering by Price Range and Model Type \n 4- Most Expensive Cars List: \n To see types of cars, press 5: \n To see the graphic of price of chosen models, press 6: \n To see best speedy cars, press 7: \n "))
     
    if choice==1:
        forza.modelType()
    elif choice==2:
        forza.priceCar()
    elif choice==3:
        forza.price_model()
    elif choice==4:
        forza.expensive()
    elif choice==5:
        forza.see_typesofcars() 
    elif choice==6:
        forza.graph_models()
    elif choice==7:
        forza.speed()
    elif choice==8:
        forza.year_of_cars()
    else:
        
        break