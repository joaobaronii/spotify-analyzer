from auth import criar_cliente
from analysis import estilo_artistas, estilo_musicas, musicas_mais_ouvidas, artistas_mais_ouvidos

def escolhaTimeRange():
    print("1- Último ano\n2- Últimos 6 meses\n3- Últimas 4 semanas")
    time_range = int(input("Escolha o tempo a ser considerado: "))
    match time_range:
        case 1:
            return 'long_term'
        case 2:
            return 'medium_term'
        case 3:
            return 'short_term'
        case _:
            print("Opção inválida. Usando 6 meses como padrão.")
            return 'medium_term'
        
def menu():
    sp = criar_cliente()

    while True:
        print("-"*40)
        print("Escolha uma opção:")
        print("1- Mostrar estilos com base em artistas")
        print("2- Mostrar estilos com base em músicas")
        print("3- Mostrar artistas")
        print("4- Mostrar músicas")
        print("5- Sair")
        
        opcao = int(input("Escolha uma opção: "))

        match opcao:
            case 1:
                time_range = escolhaTimeRange()
                estilo_artistas(sp, time_range)
            case 2:
                time_range = escolhaTimeRange()
                estilo_musicas(sp, time_range)
            case 3:
                time_range = escolhaTimeRange()
                musicas_mais_ouvidas(sp, time_range)
            case 4:
                time_range = escolhaTimeRange()
                artistas_mais_ouvidos(sp, time_range)
            case 5:
                print("Saindo...")
                break
            case _:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    print("Bem-vindo ao Spotify Analyzer!")
    menu()