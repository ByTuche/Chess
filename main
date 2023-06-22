import pygame

# Constants for the board
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640
SQUARE_SIZE = SCREEN_WIDTH // 8


piece_images = {
    'R': './assets/b_rook.png',
    'N': './assets/b_knight.png',
    'F': './assets/b_fou.png',
    'Q': './assets/b_queen.png',
    'K': './assets/b_king.png',
    'P': './assets/b_pawn.png',
    'r': './assets/w_rook.png',
    'n': './assets/w_knight.png',
    'f': './assets/w_fou.png',
    'q': './assets/w_queen.png',
    'k': './assets/w_king.png',
    'p': './assets/w_pawn.png'
}

def initialize_board():
    board = [
        ['r', 'n', 'f', 'q', 'k', 'f', 'n', 'r'],
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        ['R', 'N', 'F', 'Q', 'K', 'F', 'N', 'R']
    ]
    return board

def draw_board(screen):
    for row in range(8):
        for col in range(8):
            x = col * SQUARE_SIZE
            y = row * SQUARE_SIZE
            color = (255, 207, 159) if (row + col) % 2 == 0 else (210, 140, 69)
            pygame.draw.rect(screen, color, (x, y, SQUARE_SIZE, SQUARE_SIZE))


def draw_pieces(screen, board):
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece != ' ':
                piece_image = pygame.image.load(piece_images[piece])
                piece_image = pygame.transform.scale(piece_image, PIECE_SIZE)  # Resize the piece image
                x = col * SQUARE_SIZE 
                y = row * SQUARE_SIZE 
                screen.blit(piece_image, (x, y))
                # Draw the piece image at (x, y) position

def is_valid_move(selected_row, selected_col, dest_row, dest_col):
    piece = board[selected_row][selected_col]
    if selected_row == dest_row and selected_col == dest_col:
        return False
    # Check if the destination position is within the board boundaries
    if dest_row < 0 or dest_row >= 8 or dest_col < 0 or dest_col >= 8:
        return False

    if board[dest_row][dest_col].isupper() != piece.isupper() or board[dest_row][dest_col] == ' ':#si la piece n'est pas une piece alliée
        
        if piece == "p": #si la piece est un pion blanc
            if dest_row > selected_row: #si la ligne de destination est supérieur à la ligne actuelle
                if selected_col == dest_col and board[dest_row][dest_col] == ' ': #si le pion reste sur la meme colonne et qu'il y a du vide devant lui
                    if selected_row == 1 and board[selected_row + 1][selected_col] == ' ' : #si le pion est sur sa ligne de départ
                        if dest_row <=3: #si le pion n'avance pas de plus de 2 cases
                            return True #alors il peut bouger
                    else: #si le pion n'est pas sur sa ligne de départ 
                        if dest_row -1 == selected_row: #si la destination est d'une case
                            return True #alors le pion peut bouger
                if selected_col == dest_col -1 or selected_col == dest_col +1 : #si la piece se déplace d'une seule colonne
                    if dest_row - 1 == selected_row:  #et d'une seule ligne
                        if board[dest_row][dest_col] != ' ': #si la case visé ne contient pas de vide
                            return True
        
        if piece == "P":#si la piece est un pion noir
            if dest_row < selected_row: #si la ligne de destination est supérieur à la ligne actuelle
                if selected_col == dest_col and board[dest_row][dest_col] == ' ': #si le pion reste sur la meme colonne et qu'il y a du vide devant lui
                    if selected_row == 6 : #si le pion est sur sa ligne de départ
                        if dest_row >=4: #si le pion n'avance pas de plus de 2 cases
                            return True #alors il peut bouger
                    else: #si le pion n'est pas sur sa ligne de départ 
                        if dest_row + 1 == selected_row: #si la destination est à une seule case
                            return True #alors le pion peut bouger
                if selected_col == dest_col -1 or selected_col == dest_col +1 : #si la piece se déplace d'une seule colonne
                    if dest_row + 1 == selected_row:  #et d'une seule ligne
                        if board[dest_row][dest_col] != ' ': #si la case visé ne contient pas de vide
                            if board[dest_row][dest_col].isupper() != piece.isupper(): #si la piece est d'une couleur différente
                                return True
        
        if piece in ['r','R','q','Q']: #si la piece est une tour 
            if dest_row == selected_row : #si la tour se déplace sur sa ligne
                if dest_col < selected_col:
                    for cases in range(selected_col-1,dest_col,-1):
                        if board[dest_row][cases] != ' ' :#si l'une des cases sur le chemin contient une piece
                            return False #alors la piece ne bouge pas
                if dest_col > selected_col:
                    for cases in range(selected_col+1,dest_col):
                        if board[dest_row][cases] != ' ' :#si l'une des cases sur le chemin contient une piece
                            return False #alors la piece ne bouge pas

                return True#sinon, oui
            
                
            if dest_col == selected_col : #si la tour se déplace sur sa colonne
                if dest_row < selected_row:
                    for cases in range(selected_row-1,dest_row,-1):
                        if board[cases][dest_col] != ' ' :#si l'une des cases sur le chemin contient une piece
                            return False #alors la piece ne bouge pas
                if dest_row > selected_row:
                    for cases in range(selected_row+1,dest_row):
                        if board[cases][dest_col] != ' ' :#si l'une des cases sur le chemin contient une piece
                            return False #alors la piece ne bouge pas
                return True#sinon, oui
                
        if piece == "n" or piece == 'N':#si piece est un cavalier
            #on autorise les 8 positions de déplacement du chevalier si elle sont possibles
            if board[dest_row][dest_col].isupper() != piece.isupper() or board[dest_row][dest_col] == ' ':
                
                if selected_row+2 < 8 and selected_col+1 < 8 :
                    if selected_row + 2 == dest_row and selected_col+1 == dest_col:
                        return True
                if selected_row+2 < 8 and selected_col-1 >= 0:
                    if selected_row + 2 == dest_row and selected_col-1 == dest_col:
                        return True
                if selected_row+1 < 8 and selected_col+2 < 8 :
                    if selected_row + 1 == dest_row and selected_col+2 == dest_col:
                        return True
                if selected_row+1 < 8 and selected_col-2 >= 0:
                    if selected_row + 1 == dest_row and selected_col-2 == dest_col:
                        return True
                if selected_row-2 >= 0 and selected_col+1 < 8 :
                    if selected_row - 2 == dest_row and selected_col+1 == dest_col:
                        return True
                if selected_row-2 >= 0 and selected_col-1 >= 0:
                    if selected_row - 2 == dest_row and selected_col-1 == dest_col:
                        return True
                if selected_row-1 >= 0 and selected_col+2 < 8 :
                    if selected_row - 1 == dest_row and selected_col+2 == dest_col:
                        return True
                if selected_row-1 >= 0 and selected_col-2 >= 0:
                    if selected_row - 1 == dest_row and selected_col-2 == dest_col:
                        return True

        if piece in ['f', 'F','q','Q']:
            
            for i in range(1,8):
                if selected_row + i < 8 and selected_col + i < 8:
                    if dest_row == selected_row + i and dest_col == selected_col + i:
                        for cases in range(1,i):
                            if board[selected_row + cases][selected_col + cases] != ' ':
                                return False
                        return True
                if selected_row + i < 8 and selected_col - i >= 0:
                    if dest_row == selected_row + i and dest_col == selected_col - i:
                        for cases in range(1,i):
                            if board[selected_row + cases][selected_col - cases] != ' ':
                                return False
                        return True
                if selected_row - i >= 0 and selected_col + i < 8:
                    if dest_row == selected_row - i and dest_col == selected_col + i:
                        for cases in range(1,i):
                            if board[selected_row - cases][selected_col + cases] != ' ':
                                return False
                        return True
                if selected_row - i >= 0 and selected_col - i >= 0:
                    if dest_row == selected_row - i and dest_col == selected_col - i:
                        for cases in range(1,i):
                            if board[selected_row - cases][selected_col - cases] != ' ':
                                return False
                        return True
        if piece in ['k','K']:
            if dest_row in [selected_row + 1,selected_row ,selected_row - 1] and dest_col in [selected_col + 1,selected_col ,selected_col - 1]:
                return True
                             

    else:
        return False
    

def destination_choice(selected_piece):
    cpt = 0
    for row in range(8):
        for col in range(8):
            if is_valid_move(selected_piece[0],selected_piece[1], row, col):
                x = col * SQUARE_SIZE + SQUARE_SIZE // 2
                y = row * SQUARE_SIZE + SQUARE_SIZE // 2
                moves = pygame.draw.circle(screen, [0, 255, 0], (x, y), SQUARE_SIZE // 2 - 30)
                cpt += 1
    return cpt

def move_piece(selected_row, selected_col, dest_row, dest_col):
    piece = board[selected_row][selected_col]
    board[selected_row][selected_col] = ' '  # Empty the source position
    board[dest_row][dest_col] = piece  # Move the piece to the destination position

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
PIECE_SIZE = (SQUARE_SIZE, SQUARE_SIZE)  # Adjust the size as needed

# Initialize the board
board = initialize_board()

running = True
tour = 0
while running:
    draw_board(screen)
    draw_pieces(screen, board)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                mouse_pos = pygame.mouse.get_pos()
                selected_row = mouse_pos[1] // SQUARE_SIZE
                selected_col = mouse_pos[0] // SQUARE_SIZE
                selected_piece = None
                if board[selected_row][selected_col] == ' ':
                    break
                selected_piece = (selected_row, selected_col)
                if board[selected_row][selected_col].isupper() == True and tour % 2 == 0:
                    break
                if board[selected_row][selected_col].isupper() == False and tour % 2 != 0:
                    break
                    
                destination_piece = None
                pygame.event.clear(pygame.MOUSEBUTTONDOWN)
                if destination_choice(selected_piece) == 0:
                    break
                pygame.display.flip()
                while destination_piece == None:  
                    for dest in pygame.event.get():
                        if dest.type == pygame.MOUSEBUTTONDOWN:
                            if event.button == 1:
                                mouse_pos = pygame.mouse.get_pos()

                                destination_row = mouse_pos[1] // SQUARE_SIZE
                                destination_col = mouse_pos[0] // SQUARE_SIZE
                                destination_piece = (destination_row, destination_col)
                                if destination_piece == selected_piece: 
                                    break
                            if selected_piece != None:
                                if is_valid_move(selected_row, selected_col, destination_row, destination_col):
                                    move_piece(selected_row, selected_col, destination_row, destination_col)
                                    tour += 1
                                

        if event.type == pygame.QUIT:
                    running = False

    
    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()
