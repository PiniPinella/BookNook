from typing import List, Optional 
import sqlite3
from fastapi import FastAPI, HTTPException, APIRouter
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware