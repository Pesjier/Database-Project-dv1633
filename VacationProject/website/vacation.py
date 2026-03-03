from flask import Blueprint, request, render_template, redirect, url_for
import mysql.connector

vacation = Blueprint("vacation", __name__)