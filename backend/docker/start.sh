echo "Waiting database"

while ! nc -z postgresql 5432; do
    sleep 0.1
done

echo "Database initilized"

echo "Initializing app"

python3 /backend/main.py

