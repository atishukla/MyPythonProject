class Enemy():
    def shift_right(self):
        print('Enemy Shift Right...')

    def shift_left(self):
        print('Enemy Shift Left...')


class Ninja(Enemy):
    def karate_chop(self):
        print('Karate Chop !')


class Zombie(Enemy):
    def bite(self):
        print('I am biting..')


# This shows that nimja and zombie has access to enemy class.
enemy = Enemy()
enemy.shift_left()


ninja = Ninja()
ninja.karate_chop()
ninja.shift_right()


zombie = Zombie()
zombie.shift_right()
zombie.shift_left()