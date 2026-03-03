from flask import Blueprint, request, render_template, redirect, url_for
import mysql.connector

city = Blueprint("city", __name__)