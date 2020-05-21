from PyInquirer import prompt, Separator
from examples import custom_style_2

Ingredient_cost={'ham':0.8,'pineapple':0.5, 'meatball':1.0, 'bacon':0.7, 'mushroom':1.0, 'olives':1.5, 'Pizza crust':1.0, 'Cheese':0.8, 'tomatoes':0.7, 'pepperoni':0.7, 'parsley':0.8, 'Spaghetti':1.0}

class Food:
    total_items=0
    cost=0
    def __init__(self):
        pass

    def foodName(self):
        return self.name

    def foodCategory(self):
        non_veg_list=['ham','meatball','bacon','pepperoni']
        check=any(item in self.ingredients for item in non_veg_list)
        if check is True:
            return 'Nonveg'
        else:
            return 'Veg'    

    def foodType(self):
        self.foodCategory()
        return (self.category+" "+self.name)

    def calCost(self):
        cost=0
        for ingredient in self.ingredients:
            cost+=Ingredient_cost[ingredient]
        return cost   

class Pizza(Food):
    def __init__(self,*ingredients):
        self.name="Pizza"
        self.ingredients=ingredients
        self.category=self.foodCategory()
        Food.total_items+=1
        self.cost=self.calCost()
        Food.cost+=self.cost

    @classmethod
    def Mexican(cls):
        ingredients=['Pizza crust', 'Cheese', 'ham', 'olives']
        return cls(*ingredients)

    @classmethod
    def SpiceHeaven(cls):
        ingredients=['Pizza crust', 'Cheese', 'meatball', 'bacon']
        return cls(*ingredients)    

class Pasta(Food):
    def __init__(self,*ingredients):
        self.name="Pasta"
        self.ingredients=ingredients
        self.category=self.foodCategory()
        Food.total_items+=1
        self.cost=self.calCost()
        Food.cost+=self.cost

    @classmethod
    def Sicilian(cls):
        ingredients=['Spaghetti', 'Cheese', 'pepperoni', 'parsley']
        return cls(*ingredients)

    @classmethod
    def SweetCream(cls):
        ingredients=['Spaghetti', 'Cheese', 'meatball', 'tomatoes']
        return cls(*ingredients)     
    
print('Hi, welcome to Python Foodstore')

items=[]
order=Food()
while(True):
    question1 = [
        {
            'type': 'list',
            'name': 'foodtype',
            'message': 'What do you want to order?',
            'choices': ['Pizza', 'Pasta']
        }
    ]
    answers = prompt(question1, style=custom_style_2)
    if answers['foodtype']=='Pizza':
        question2 = [
            {
                'type': 'list',
                'name': 'precustom',
                'message': 'Choose one of the following- ',
                'choices': ['Predefined Ingredients', 'Custom Ingredients']
            }
        ]
        answers=prompt(question2, style=custom_style_2)
        if answers['precustom']=='Predefined Ingredients':
            question3 = [
                {
                    'type': 'list',
                    'name': 'type',
                    'message': 'Choose type of Pizza- ',
                    'choices': ['Mexican', 'Spice Heaven']
                }
            ]
            answers=prompt(question3, style=custom_style_2)
            if answers['type']=='Mexican':
                items.append(Pizza.Mexican())
            else:
                items.append(Pizza.SpiceHeaven())
        else:
            questions = [
                {
                    'type': 'checkbox',
                    'message': 'Select Ingredients',
                    'name': 'ingredients',
                    'choices': [ 
                        Separator('= Base Ingredients ='),
                        {
                            'name': 'Pizza crust',
                            'disabled':'Must be included'
                        },
                        {
                            'name': 'Cheese',
                            'disabled':'Must be included'
                        },
                        Separator('= Veg ='),
                        {
                            'name': 'pineapple'
                        },
                        {
                            'name': 'mushroom'
                        },
                        {
                            'name': 'olives'
                        },
                        Separator('= Non Veg ='),
                        {
                            'name': 'ham',
                        },
                        {
                            'name': 'meatball'
                        },
                        {
                            'name': 'bacon'
                        },
                    ],
                }
            ]            
            answers = prompt(questions, style=custom_style_2)
            answers['ingredients'].insert(0,'Cheese')
            answers['ingredients'].insert(0,'Pizza crust')
            items.append(Pizza(*answers['ingredients']))
    else:
        question2 = [
            {
                'type': 'list',
                'name': 'precustom',
                'message': 'Choose one of the following- ',
                'choices': ['Predefined Ingredients', 'Custom Ingredients']
            }
        ]
        answers=prompt(question2, style=custom_style_2)
        if answers['precustom']=='Predefined Ingredients':
            question3 = [
                {
                    'type': 'list',
                    'name': 'type',
                    'message': 'Choose type of Pasta- ',
                    'choices': ['Sicilian', 'Sweet cream']
                }
            ]
            answers=prompt(question3, style=custom_style_2)
            if answers['type']=='Sicilian':
                items.append(Pasta.Sicilian())
            else:
                items.append(Pasta.SweetCream())
        else:
            questions = [
                {
                    'type': 'checkbox',
                    'message': 'Select Ingredients',
                    'name': 'ingredients',
                    'choices': [ 
                        Separator('= Base Ingredients ='),
                        {
                            'name': 'Spaghetti',
                            'disabled':'Must be included'
                        },
                        {
                            'name': 'Cheese',
                            'disabled':'Must be included'
                        },
                        Separator('= Veg ='),
                        {
                            'name': 'tomatoes'
                        },
                        {
                            'name': 'mushroom'
                        },
                        {
                            'name': 'parsley'
                        },
                        Separator('= Non Veg ='),
                        {
                            'name': 'ham',
                        },
                        {
                            'name': 'meatball'
                        },
                        {
                            'name': 'pepperoni'
                        },
                    ],
                }
            ]            
            answers = prompt(questions, style=custom_style_2)
            answers['ingredients'].insert(0,'Cheese')
            answers['ingredients'].insert(0,'Spaghetti')
            items.append(Pasta(*answers['ingredients']))
    questions=[
        {
            'type': 'confirm',
            'message': 'Do you want to continue?',
            'name': 'continue',
            'default': True,
        }
    ]
    ans=prompt(questions,style=custom_style_2)
    if ans['continue']==False:
        break

for item in items:
    print("Item Ingredients- ",end='')
    print(item.ingredients)
    print("Item type- "+item.foodType())
    print("Item cost- $"+str(item.cost)+"\n")   

print("\nTotal items- "+ str(order.total_items))
print("Total Cost- $"+str(order.cost))