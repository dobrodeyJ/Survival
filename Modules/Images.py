import pygame

class Images:
    def __init__(self):
        self.__createDict()

    def __createDict(self):
        path = "resource/"

        """Textures"""
        WoodBox = pygame.image.load(path + "texture/textures_Sand/3.png")
        Box = pygame.image.load(path + "texture/textures_Sand/22.png")
        PortalIn = pygame.image.load(path + "texture/Portals/portal.png")
        PortalOut = pygame.image.load(path + "texture/Portals/portal2.png")
        DestroyOne = pygame.image.load(path + "texture/textures_Sand/33.png")
        DestroyTwo = pygame.image.load(path + "texture/textures_Sand/333.png")
        Grass = pygame.image.load(path + "texture/textures_Sand/00.png")
        background = pygame.image.load(path + "texture/textures_Sand/fon.jpg")
        topBar = pygame.image.load(path + "texture/BG/TOP_bar3.jpg")
        Plita = pygame.image.load(path + "texture/Plitka2.jpg")

        """Heroes"""
        playerOne_down1 = pygame.image.load(path + "Players/heroes2/hero_down1.png")
        playerOne_down2 = pygame.image.load(path + "Players/heroes2/hero_down2.png")
        playerOne_down3 = pygame.image.load(path + "Players/heroes2/hero_down3.png")
        playerOne_left1 = pygame.image.load(path + "Players/heroes2/hero_left1.png")
        playerOne_left2 = pygame.image.load(path + "Players/heroes2/hero_left2.png")
        playerOne_left3 = pygame.image.load(path + "Players/heroes2/hero_left3.png")
        playerOne_right1 = pygame.image.load(path + "Players/heroes2/hero_right1.png")
        playerOne_right2 = pygame.image.load(path + "Players/heroes2/hero_right2.png")
        playerOne_right3 = pygame.image.load(path + "Players/heroes2/hero_right3.png")
        playerOne_up1 = pygame.image.load(path + "Players/heroes2/hero_up1.png")
        playerOne_up2 = pygame.image.load(path + "Players/heroes2/hero_up2.png")
        playerOne_up3 = pygame.image.load(path + "Players/heroes2/hero_up3.png")

        fireBall1 = pygame.image.load(path + "Atacks/FireBall/1.png")
        fireBall2 = pygame.image.load(path + "Atacks/FireBall/2.png")
        fireBall3 = pygame.image.load(path + "Atacks/FireBall/3.png")
        fireBall4 = pygame.image.load(path + "Atacks/FireBall/4.png")
        fireBall5 = pygame.image.load(path + "Atacks/FireBall/5.png")

        fireBallTwo = pygame.image.load(path + "Atacks/fireBall2.png")

        """Bots"""
        zombie_down1 = pygame.image.load(path +  "Bots/zombies/zombie_down1.png")
        zombie_down2 = pygame.image.load(path +  "Bots/zombies/zombie_down2.png")
        zombie_down3 = pygame.image.load(path +  "Bots/zombies/zombie_down3.png")
        zombie_left1 = pygame.image.load(path +  "Bots/zombies/zombie_left1.png")
        zombie_left2 = pygame.image.load(path +  "Bots/zombies/zombie_left2.png")
        zombie_left3 = pygame.image.load(path +  "Bots/zombies/zombie_left3.png")
        zombie_right1 = pygame.image.load(path + "Bots/zombies/zombie_right1.png")
        zombie_right2 = pygame.image.load(path + "Bots/zombies/zombie_right2.png")
        zombie_right3 = pygame.image.load(path + "Bots/zombies/zombie_right3.png")
        zombie_up1 = pygame.image.load(path +    "Bots/zombies/zombie_up1.png")
        zombie_up2 = pygame.image.load(path +    "Bots/zombies/zombie_up2.png")
        zombie_up3 = pygame.image.load(path +    "Bots/zombies/zombie_up3.png")
        spider_left1 = pygame.image.load(path +    "Bots/spider/spider_left_1.png")
        spider_left2 = pygame.image.load(path +    "Bots/spider/spider_left_2.png")
        spider_left3 = pygame.image.load(path +    "Bots/spider/spider_left_3.png")
        spider_right1 = pygame.image.load(path +    "Bots/spider/spider_right_1.png")
        spider_right2 = pygame.image.load(path +    "Bots/spider/spider_right_2.png")
        spider_right3 = pygame.image.load(path +    "Bots/spider/spider_right_3.png")
        spider_up1 = pygame.image.load(path +    "Bots/spider/spider_up_1.png")
        spider_up2 = pygame.image.load(path +    "Bots/spider/spider_up_2.png")
        spider_up3 = pygame.image.load(path +    "Bots/spider/spider_up_3.png")
        spider_down1 = pygame.image.load(path +    "Bots/spider/spider_down_1.png")
        spider_down2 = pygame.image.load(path +    "Bots/spider/spider_down_2.png")
        spider_down3 = pygame.image.load(path +    "Bots/spider/spider_down_3.png")


        """Health"""
        health_heroes_full = pygame.image.load(path + "Health/HealthHeroe/health_full.png")
        health_heroes_null = pygame.image.load(path + "Health/HealthHeroe/health_null.png")
        health_heroes_1 = pygame.image.load(path + "Health/HealthHeroe/health1.png")
        health_heroes_2 = pygame.image.load(path + "Health/HealthHeroe/health2.png")
        health_heroes_3 = pygame.image.load(path + "Health/HealthHeroe/health3.png")
        health_heroes_4 = pygame.image.load(path + "Health/HealthHeroe/health4.png")
        health_heroes_5 = pygame.image.load(path + "Health/HealthHeroe/health5.png")
        health_heroes_6 = pygame.image.load(path + "Health/HealthHeroe/health6.png")
        health_heroes_7 = pygame.image.load(path + "Health/HealthHeroe/health7.png")
        health_heroes_8 = pygame.image.load(path + "Health/HealthHeroe/health8.png")
        health_heroes_9 = pygame.image.load(path + "Health/HealthHeroe/health9.png")
        health_heroes_10 = pygame.image.load(path + "Health/HealthHeroe/health10.png")
        health_heroes_11 = pygame.image.load(path + "Health/HealthHeroe/health11.png")
        health_heroes_12 = pygame.image.load(path + "Health/HealthHeroe/health12.png")
        health_heroes_13 = pygame.image.load(path + "Health/HealthHeroe/health13.png")
        health_heroes_14 = pygame.image.load(path + "Health/HealthHeroe/health14.png")
        health_heroes_15 = pygame.image.load(path + "Health/HealthHeroe/health15.png")
        health_heroes_16 = pygame.image.load(path + "Health/HealthHeroe/health16.png")
        health_heroes_17 = pygame.image.load(path + "Health/HealthHeroe/health17.png")
        health_heroes_18 = pygame.image.load(path + "Health/HealthHeroe/health18.png")
        health_heroes_19 = pygame.image.load(path + "Health/HealthHeroe/health19.png")

        health_zombie_full = pygame.image.load(path + "Health/HealthBots/health_full.png")
        health_zombie_null = pygame.image.load(path + "Health/HealthBots/health_null.png")
        health_zombie_1 = pygame.image.load(path + "Health/HealthBots/health1.png")
        health_zombie_2 = pygame.image.load(path + "Health/HealthBots/health2.png")

        """PointRespawn"""
        PointRespawnZombies = pygame.image.load(path + "texture/Portals/respZombie.png")
        PointRespawnSpider = pygame.image.load(path + "texture/Portals/respSpider.png")

        portalWin = pygame.image.load(path + "texture/Portals/PortalWin/TP2.png")

        meat =  pygame.image.load(path + "texture/MeatWins/MEAT1.png")
        win = pygame.image.load(path + "texture/MeatWins/win1.png")

        menu_bg = pygame.image.load(path + "texture/MENU/menu fon.jpg")
        startUp = pygame.image.load(path + "texture/MENU/startUp.png")
        startDown = pygame.image.load(path + "texture/MENU/startDown.png")
        exitUp = pygame.image.load(path + "texture/MENU/exitUp.png")
        exitDown = pygame.image.load(path + "texture/MENU/exitDown.png")
        self.__images = {
            100: WoodBox,
            200: Box,
            300: PortalIn,
            400: PortalOut,
            500: Plita,
            700: DestroyOne,
            800: DestroyTwo,
            900: Grass,
            "background":    background,
            "top_bar":       topBar,
            "magian_down1":  playerOne_down1,
            "magian_down2":  playerOne_down2,
            "magian_down3":  playerOne_down3,
            "magian_left1":  playerOne_left1,
            "magian_left2":  playerOne_left2,
            "magian_left3":  playerOne_left3,
            "magian_right1": playerOne_right1,
            "magian_right2": playerOne_right2,
            "magian_right3": playerOne_right3,
            "magian_up1":    playerOne_up1,
            "magian_up2":    playerOne_up2,
            "magian_up3":    playerOne_up3,
            "fireBall1":      fireBall1,
            "fireBall2":      fireBall2,
            "fireBall3":      fireBall3,
            "fireBall4":      fireBall4,
            "fireBall5":      fireBall5,

            "fireBallTwo":     fireBallTwo,

            "health_full": health_heroes_full,
            "health_null": health_heroes_null,
            "health1":     health_heroes_1,
            "health2":     health_heroes_2,
            "health3":     health_heroes_3,
            "health4":     health_heroes_4,
            "health5":     health_heroes_5,
            "health6":     health_heroes_6,
            "health7":     health_heroes_7,
            "health8":     health_heroes_8,
            "health9":     health_heroes_9,
            "health10":    health_heroes_10,
            "health11":    health_heroes_11,
            "health12":    health_heroes_12,
            "health13":    health_heroes_13,
            "health14":    health_heroes_14,
            "health15":    health_heroes_15,
            "health16":    health_heroes_16,
            "health17":    health_heroes_17,
            "health18":    health_heroes_18,
            "health19":    health_heroes_19,

            "zombie_down1":  zombie_down1,
            "zombie_down2":  zombie_down2,
            "zombie_down3":  zombie_down3,
            "zombie_left1":  zombie_left1,
            "zombie_left2":  zombie_left2,
            "zombie_left3":  zombie_left3,
            "zombie_right1": zombie_right1,
            "zombie_right2": zombie_right2,
            "zombie_right3": zombie_right3,
            "zombie_up1":    zombie_up1,
            "zombie_up2":    zombie_up2,
            "zombie_up3":    zombie_up3,
            "zombie_health_1":    health_zombie_1,
            "zombie_health_2":    health_zombie_2,
            "zombie_health_full": health_zombie_full,
            "zombie_health_null": health_zombie_null,
            "respawn_zombies":    PointRespawnZombies,

            "spider_down1":  spider_down1,
            "spider_down2":  spider_down2,
            "spider_down3":  spider_down3,
            "spider_left1":  spider_left1,
            "spider_left2":  spider_left2,
            "spider_left3":  spider_left3,
            "spider_right1": spider_right1,
            "spider_right2": spider_right2,
            "spider_right3": spider_right3,
            "spider_up1":    spider_up1,
            "spider_up2":    spider_up2,
            "spider_up3":    spider_up3,
            "respawn_spider": PointRespawnSpider,
            "portalWin":   portalWin,
            "MEAT":        meat,
            "WIN":         win,
            "menuBG":      menu_bg,
            "startUp":     startUp,
            "startDown":   startDown,
            "exitUp" :     exitUp,
            "exitDown" :   exitDown
        }

    def getImage(self, key):
        return self.__images[key]