from ui.ui import UI
from services.service import Service


def main():
    service = Service()
    UI(service=service)


if __name__ == "__main__":
    main()
