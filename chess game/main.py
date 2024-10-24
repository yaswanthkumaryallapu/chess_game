import pygame
import chess
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
SQUARE_SIZE = WIDTH // 8
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load Images
PIECES = {}


def load_images():
    PIECES['white_king'] = pygame.image.load('assets/white_king.png')
    PIECES['white_queen'] = pygame.image.load('assets/white_queen.png')
    PIECES['white_rook'] = pygame.image.load('assets/white_rook.png')
    PIECES['white_bishop'] = pygame.image.load('assets/white_bishop.png')
    PIECES['white_knight'] = pygame.image.load('assets/white_knight.png')
    PIECES['white_pawn'] = pygame.image.load('assets/white_pawn.png')
    PIECES['black_king'] = pygame.image.load('assets/black_king.png')
    PIECES['black_queen'] = pygame.image.load('assets/black_queen.png')
    PIECES['black_rook'] = pygame.image.load('assets/black_rook.png')
    PIECES['black_bishop'] = pygame.image.load('assets/black_bishop.png')
    PIECES['black_knight'] = pygame.image.load('assets/black_knight.png')
    PIECES['black_pawn'] = pygame.image.load('assets/black_pawn.png')


# Draw chessboard
def draw_chessboard(window):
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(window, color, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


# Constants for piece name mapping
PIECE_TYPES = {
    'k': 'king',
    'q': 'queen',
    'r': 'rook',
    'b': 'bishop',
    'n': 'knight',
    'p': 'pawn'
}


# Map piece symbols to their image file names
def get_piece_image(piece):
    if piece.isupper():  # White piece
        color = 'white'
    else:  # Black piece
        color = 'black'

    piece_type = PIECE_TYPES[piece.lower()]
    return PIECES[f'{color}_{piece_type}']


# Draw pieces on the chessboard
def draw_pieces(window, board):
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            col = square % 8
            row = square // 8
            piece_image = get_piece_image(piece.symbol())
            window.blit(pygame.transform.scale(piece_image, (SQUARE_SIZE, SQUARE_SIZE)),
                        pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


def show_message(window, message):
    pygame.draw.rect(window, BLACK, pygame.Rect(100, 450, 800, 100))
    font = pygame.font.SysFont('comicsans', 50)
    text_surface = font.render(message, True, WHITE)
    window.blit(text_surface, (120, 470))
    pygame.display.update()
    pygame.time.delay(3000)


def main():
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Multiplayer Chess')

    while True:
        board = chess.Board()
        load_images()  # Load chess piece images
        selected_square = None
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    col = x // SQUARE_SIZE
                    row = y // SQUARE_SIZE
                    square = chess.square(col, row)

                    if selected_square is None:  # Select a piece
                        if board.piece_at(square):
                            selected_square = square
                    else:  # Move the selected piece
                        if square != selected_square:
                            move = chess.Move(selected_square, square)
                            if move in board.legal_moves:
                                board.push(move)
                                if board.is_checkmate():
                                    show_message(window, "Checkmate! Restarting the game.")
                                    running = False  # Break the main loop to restart game
                        selected_square = None

            # Draw board and pieces
            draw_chessboard(window)
            draw_pieces(window, board)

            pygame.display.update()


if __name__ == "__main__":
    main()
