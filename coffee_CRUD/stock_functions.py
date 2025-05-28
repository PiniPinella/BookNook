from fastapi import FastAPI, HTTPException, APIRouter
from typing import List
import sqlite3

#### self made 
from helper_functions import get_coffee_connection , row_to_stock
from classes import Stock, StockAdjust


#### connect router via API 
stock_router = APIRouter(prefix="/stock")

@stock_router.get("/", response_model=List[Stock])
def get_full_stock():
    """Returns all stock entrys"""
    conn = get_coffee_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM stock")
        row = cursor.fetchone()

        if not row:
            raise HTTPException(status_code=404, detail="Stock data not found")

        return [row_to_stock(row) for row in cursor.fetchall()]
    finally:
        conn.close()

@stock_router.put("/stock", response_model=Stock)
def full_update_stock(stock: Stock):
    """WARNING! Overwrites all stockitems with different quantity (full input necsessary)"""
    conn = get_coffee_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE stock SET
                cow_milk = ?,
                oat_milk = ?,
                coffee_beans = ?,
                lemonade = ?,
                apple_spritzer = ?,
                water = ?
        """, (
            stock.cow_milk,
            stock.oat_milk,
            stock.coffee_beans,
            stock.lemonade,
            stock.apple_spritzer,
            stock.water
        ))
        conn.commit()

        cursor.execute("SELECT * FROM stock")
        row = cursor.fetchone()
        return row_to_stock(row)

    finally:
        conn.close()

@stock_router.patch("/stock", response_model=Stock)
def adjust_stock(adjust: StockAdjust):
    """Updates stock by adding or subtracting specified quantities for one or more items."""
    conn = get_coffee_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM stock")
        row = cursor.fetchone()

        if not row:
            raise HTTPException(status_code=404, detail="Stock data not found")

        current = dict(row)
        
        new_values = {
            key: current[key] + getattr(adjust, key)
            for key in current.keys()
        }

        # Update DB
        cursor.execute("""
            UPDATE stock SET
                cow_milk = ?,
                oat_milk = ?,
                coffee_beans = ?,
                lemonade = ?,
                apple_spritzer = ?,
                water = ?
        """, (
            new_values["cow_milk"],
            new_values["oat_milk"],
            new_values["coffee_beans"],
            new_values["lemonade"],
            new_values["apple_spritzer"],
            new_values["water"]
        ))
        conn.commit()

        # Aktualisierten Wert zurückgeben
        cursor.execute("SELECT * FROM stock")
        updated_row = cursor.fetchone()
        return row_to_stock(updated_row)

    finally:
        conn.close()