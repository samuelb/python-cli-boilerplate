import sys
from myapp.app import MyApp


if __name__ == '__main__':
    app = MyApp()
    sys.exit(app.run(sys.argv[1:]))
