import glob
from pathlib import Path
from d3vil.utils import load_plugins
import logging
from . import D3vil, D3vil2, D3vil3, D3vil5 , D3vil6, D3vil7, D3vil8, D3vil9, D3vil10

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

path = "d3vil/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("Successfully deployed!")
print("Enjoy! Do visit @d3vil")

if __name__ == "__main__":
    D3vil.run_until_disconnected()
    
if __name__ == "__main__":
    D3vil2.run_until_disconnected()

if __name__ == "__main__":
    D3vil3.run_until_disconnected()
    
if __name__ == "__main__":
    D3vil4.run_until_disconnected()

if __name__ == "__main__":
    D3vil5.run_until_disconnected()
    
if __name__ == "__main__":
    D3vil6.run_until_disconnected()

if __name__ == "__main__":
    D3vil7.run_until_disconnected()
    
if __name__ == "__main__":
    D3vil8.run_until_disconnected()

if __name__ == "__main__":
    D3vil9.run_until_disconnected()
    
if __name__ == "__main__":
    D3vil10.run_until_disconnected()
