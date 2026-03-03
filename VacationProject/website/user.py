from flask import Blueprint, request, render_template, redirect, url_for
import mysql.connector

user = Blueprint("user", __name__)