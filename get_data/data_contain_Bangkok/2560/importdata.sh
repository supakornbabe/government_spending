for f in *.json
do
echo "Processing $f file...";
mongoimport --type json --file $f --collection government --db stat_for_application && mv $f P-$f;
done