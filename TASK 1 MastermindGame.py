import random
number=random.randrange(1000,10000)
print("\n___________________________MASTERMIND GAME__________________________\n")
print("Number guessed by Computer:",number,"\n")
chances=5
guess_number=int(input(f'Guess a 4 digit number, you have {chances} chances left: '))
if guess_number==number:
    print("\nGreat you WON , now you are MASTERMIND")
    print("\n________________________MASTERMIND GAME ENDED_______________________\n")
else:
    trials=0
    while guess_number != number and chances:
        trials+=1
        chances-=1
        correctdigits=0
        guess_number=str(guess_number)
        number=str(number)
        correct=['X'] *4
        for i in range(0,4):
            if guess_number[i]==number[i]:
                correctdigits+=1
                correct[i]=number[i]
        if correctdigits<4 and correctdigits>0 and chances:
            print('\nNot the correct guess, but you guessed',correctdigits,'numbers correct')
            print('Current status is:')
            for char in correct:
                print(char, end='')
            print('\n\n')
            guess_number=int(input(f'Guess a 4 digit number,you have {chances} chances left:'))
        elif correctdigits==0 and chances:
            print('\nNone of the digits you guessed is right\n\n')
            guess_number=int(input(f'Guess a 4 digit number, you have {chances} chances left: '))
    if guess_number==number:
        print("\nGreat, you WON in",trials,"guesses,now you are a MASTERMIND")
        print("\n________________________MASTERMIND GAME ENDED_______________________\n")
    if chances==0 and guess_number!=number:
        print("\nSorry , you LOST as you ran out of chances")   
        print("Number is:",number)
        print("\n________________________MASTERMIND GAME ENDED_______________________\n")