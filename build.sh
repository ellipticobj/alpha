pip3 install -U PyInstaller

echo "purging ./dist/"
rm -rf dist/
pcho "purging ./build/"
rm -rf build/

python -m PyInstaller --onefile --name "alpha-$(arch)" main.py

rm -rf "alpha-$(arch).spec"

echo "executable at dist/alpha-$(arch)"