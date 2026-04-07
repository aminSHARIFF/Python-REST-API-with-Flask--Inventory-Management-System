# Inventory Management System

A Flask REST API with a CLI interface for managing store inventory.
Built by Sharif as part of a Python REST API lab.

## Installation

1. Clone the repo:
git clone https://github.com/aminSHARIFF/Python-REST-API-with-Flask--Inventory-Management-System.git

2. Go into the folder:
cd inventory-system

3. Create and activate virtual environment:
python -m venv venv
source venv/bin/activate

4. Install dependencies:
pip install flask requests pytest

## Running the API

python app.py

## Running the CLI

Open a second terminal and run:
python cli.py

## API Endpoints

| Method | Route | Description |
|--------|-------|-------------|
| GET | /inventory | Get all items |
| GET | /inventory/<id> | Get one item |
| POST | /inventory | Add new item |
| PATCH | /inventory/<id> | Update item |
| DELETE | /inventory/<id> | Delete item |
| GET | /lookup/<barcode> | Lookup product from OpenFoodFacts |

## CLI Menu Options

1. View all inventory
2. View single item
3. Add new item
4. Update item price or quantity
5. Delete item
6. Lookup product by barcode from OpenFoodFacts API
7. Exit

## Running Tests

pytest test_app.py -v

## External API

This project uses the OpenFoodFacts API to fetch real product data by barcode.
No API key needed - it is free and open.
Example: https://world.openfoodfacts.org/api/v0/product/123456.json