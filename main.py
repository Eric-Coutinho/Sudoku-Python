import games.eleven_nine
import games.sudoku

if __name__ == "__main__":
    isPlaying = False
    while isPlaying == False:
        choice = input("Qual jogo você quer jogar? \n119\nSudoku")
        
        match choice:
            case "119":
                games.eleven_nine.playEleven_nine()
                isPlaying = True
            case "Sudoku":
                games.sudoku.playSudoku()
                isPlaying = True
            case _: 
                print('Opção inválida, tente novamente')
