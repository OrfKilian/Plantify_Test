from flask import Blueprint, jsonify, current_app, request
import mysql.connector

def get_db_cursor():
    connection = mysql.connector.connect(**current_app.config['DB_CONFIG'])
    cursor = connection.cursor(dictionary=True)
    return connection, cursor

def fetch_query_results(query, pot_id, fetchone=False):
    """Execute a query against the SmartPlant database and return the results.

    Falls die Abfrage fehlschlägt, wird eine Fehlermeldung als JSON zurückgegeben.
    """

    try:
        connection, cursor = get_db_cursor()
        cursor.execute(query, (pot_id,))

        if fetchone:
            result = cursor.fetchone() or {}
        else:
            result = cursor.fetchall()

        cursor.close()
        connection.close()

        return jsonify(result)
    except mysql.connector.Error as err:
        # Bei einem Datenbankfehler sollen keine Dummy-Daten geliefert werden
        return jsonify({"error": str(err)}), 500

views_blueprint = Blueprint('views', __name__)

@views_blueprint.route("/ping")
def ping():
    return jsonify({"message": "API läuft"})

@views_blueprint.route("/latest-today", methods=["GET"])
def get_latest_today():
    pot_id = request.args.get('pot_id')
    query = "SELECT * FROM viw_LatestValuePerPot WHERE pot_id = %s"
    return fetch_query_results(query, pot_id)

@views_blueprint.route("/all-today", methods=["GET"])
def get_all_today():
    pot_id = request.args.get('pot_id')
    query = "SELECT * FROM viw_AllValues_Today WHERE pot_id = %s"
    return fetch_query_results(query, pot_id)

@views_blueprint.route("/sunlight-30days", methods=["GET"])
def get_sunlight_30days():
    pot_id = request.args.get('pot_id')
    query = "SELECT * FROM viw_SunlightPerDay_last30Days WHERE pot_id = %s"
    return fetch_query_results(query, pot_id)

@views_blueprint.route("/average-month", methods=["GET"])
def get_average_month():
    pot_id = request.args.get('pot_id')
    query = "SELECT * FROM viw_AverageMeasurements_MTD WHERE pot_id = %s"
    return fetch_query_results(query, pot_id)

@views_blueprint.route('/latest-value', methods=['GET'])
def get_latest_value():
    pot_id = request.args.get('pot_id')
    query = '''
        SELECT created, temperature, air_humidity, ground_humidity
        FROM viw_LatestValuePerPot
        WHERE pot_id = %s
    '''
    return fetch_query_results(query, pot_id, fetchone=True)
