class Settings():
    """\class which is used to store all game settings"""
    
    def __init__(self):
        """Settings initiaton"""
        
        #Screen settings
        self.screen_width =  800
        self.screen_height = 800
        self.screen_title = "gravity"

        #Background settings
        self.background_image = "resources/space.jpg"
        
        #Ship settings
        self.ship_weigth = 100
        self.ship_image = "resources/alien.png"
        
        #Stuff settings
        self.stuff_weigth = 2
        self.speedFactor = 0.6
        self.stuff_images = [
                        "resources/stuff1.png",
                        "resources/stuff2.png",
                        "resources/stuff3.png",
                        "resources/stuff4.png"
                        ]
