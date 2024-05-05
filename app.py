import psycopg2
from config import config
from flask import Flask, render_template, request

# Connect to the PostgreSQL database server
def connect(query, params=None):
    """Connect to the PostgreSQL database server and execute a query with parameters."""
    conn = None
    rows = []
    try:
        # Parameters are stored in a separate config file
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(query, params)
        rows = cur.fetchall()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
    return rows

# app.py
app = Flask(__name__)


# serve form web page
@app.route("/")
def form():
    return render_template('index.html')

# handle venue POST and serve result web page
@app.route('/goat-handler', methods=['POST'])
def goat_handler():
    rows = connect('SELECT animal_id FROM Animal')
    heads = ['animal_id']
    return render_template('result.html', rows=rows, heads=heads)

# handle query POST and serve result web page
@app.route('/input-handler', methods=['POST'])
# query function
def query_handler():
    rows = connect(request.form['query'])
    return render_template('result.html', rows=rows)

# handle query POST and serve result web page
@app.route('/query_1', methods=['POST'])
# query function
def query_1():
   query = """
    WITH PregnantDams AS (
    SELECT a.rfid
    FROM sessionanimaltrait sat
    JOIN Animal a ON sat.animal_id = a.animal_id
    WHERE trait_code = 847 -- Assuming trait_code 847 identifies pregnant dams
    ),
    OffspringOver10lbs AS (
    SELECT a.rfid AS offspring_rfid, a.dam
    FROM sessionanimaltrait sat
    JOIN Animal a ON sat.animal_id = a.animal_id
    WHERE trait_code = 357
      AND CASE
          WHEN sat.alpha_value ~ '^\\s*$' THEN FALSE -- Excludes empty strings and strings with only whitespace
          WHEN sat.alpha_value ~ '^[+-]?[0-9]+(\\.[0-9]+)?$' THEN sat.alpha_value::numeric > 10
          ELSE FALSE
      END
    )
    SELECT DISTINCT oo.offspring_rfid, dam.rfid AS dam_rfid
    FROM OffspringOver10lbs oo
    JOIN Animal dam ON oo.dam = dam.tag  -- Assuming dam column in offspring table references dam's tag in Animal table
    JOIN PregnantDams pd ON dam.rfid = pd.rfid;
   """
   rows = connect(query)
   heads = ['Baby Goat ID', 'Dam']
   return render_template('result.html', rows=rows, heads=heads)

# handle query POST and serve result web page
@app.route('/query_2', methods=['POST'])
# query function
def query_2():
    query = """
    SELECT dam.rfid AS dam_rfid, COUNT(s.animal_id) AS total_grafted_goats
    FROM Animal a
    JOIN sessionanimaltrait s ON a.animal_id = s.animal_id
    JOIN Animal dam ON a.dam = dam.tag -- Assuming 'dam' contains the 'tag' of the dam
    WHERE s.trait_code = 735
    GROUP BY dam.rfid
    ORDER BY total_grafted_goats DESC;
    """
    # Execute the query using the connect function which handles the database connection, execution, and fetching results.
    rows = connect(query)
    # Set up column headers for displaying the results in a table on the webpage.
    heads = ['Dam', 'Total Grafted Goats']
    # Return the HTML page 'result.html', passing the fetched data and headers for rendering the results table.
    return render_template('result.html', rows=rows, heads=heads)

# handle query POST and serve result web page
@app.route('/query_3', methods=['POST'])
# query function
def query_3():
    query = """
    SELECT sire.rfid AS sire_rfid, dam.rfid AS dam_rfid, COUNT(*) as offspring_count
    FROM Animal a
    JOIN sessionanimaltrait s ON a.animal_id = s.animal_id
    JOIN Animal sire ON a.sire = sire.tag -- Assuming 'sire' contains the 'tag' of the sire
    JOIN Animal dam ON a.dam = dam.tag -- Assuming 'dam' contains the 'tag' of the dam
    WHERE s.trait_code = 357
    AND CASE
      WHEN s.alpha_value ~ '^[+-]?[0-9]*\.?[0-9]+$' THEN s.alpha_value::numeric > 5.0
      ELSE FALSE
      END
    AND s.alpha_value IS NOT NULL
    AND (a.sire IS NOT NULL AND a.sire <> '')
    AND (a.dam IS NOT NULL AND a.dam <> '')
    GROUP BY sire.rfid, dam.rfid
    ORDER BY offspring_count DESC;
    """
    rows = connect(query)
    heads = ['Sire', 'Dam','# of Offspring']
    return render_template('result.html', rows=rows, heads=heads)

# handle query POST and serve result web page
@app.route('/query_4', methods=['POST'])
# query function
def query_4():
    query = """
   SELECT dam.rfid AS dam_rfid, COUNT(*) as offspring_count
    FROM Animal a
    JOIN sessionanimaltrait s ON a.animal_id = s.animal_id
    JOIN Animal dam ON a.dam = dam.tag -- Assuming 'dam' contains the 'tag' of the dam
    WHERE s.trait_code = 357
    AND CASE
      WHEN s.alpha_value ~ '^[+-]?[0-9]*\.?[0-9]+$' THEN s.alpha_value::numeric > 5.0
      ELSE FALSE
      END
    AND s.alpha_value IS NOT NULL
    AND (a.sire IS NOT NULL AND a.sire <> '')
    GROUP BY dam.rfid
    ORDER BY offspring_count DESC;
    """
    rows = connect(query)
    heads = ['Dam','# of Offspring']
    return render_template('result.html', rows=rows, heads=heads)

# handle query POST and serve result web page
@app.route('/query_5', methods=['POST'])
# query function
def query_5():
    query = """
    SELECT a.sire, COUNT(*) as offspring_count
    FROM Animal a
    JOIN sessionanimaltrait s ON a.animal_id = s.animal_id
    WHERE s.trait_code = 357 -- BWT trait code
    AND CASE
      WHEN s.alpha_value ~ '^[+-]?[0-9]*\.?[0-9]+$' THEN s.alpha_value::numeric > 5.0
      ELSE FALSE
      END
    AND s.alpha_value IS NOT NULL
    AND (a.sire IS NOT NULL AND a.sire<> '')
    GROUP BY a.sire
    ORDER BY offspring_count DESC;
    """
    rows = connect(query)
    heads = ['Sire','# of Offspring']
    return render_template('result.html', rows=rows, heads=heads)

# handle query POST and serve result web page
@app.route('/query_6', methods=['POST'])
# query function
def query_6():
    query = """
    SELECT dam.rfid AS dam_rfid, COUNT(*) as offspring_count
    FROM Animal a
    JOIN sessionanimaltrait s ON a.animal_id = s.animal_id
    JOIN Animal dam ON a.dam = dam.tag -- Assuming 'dam' contains the 'tag' of the dam
    WHERE s.trait_code = 357
    AND CASE
      WHEN s.alpha_value ~ '^[+-]?[0-9]*\.?[0-9]+$' THEN s.alpha_value::numeric > 8.0
      ELSE FALSE
      END
    AND s.alpha_value IS NOT NULL
    AND (a.sire IS NOT NULL AND a.sire <> '')
    GROUP BY dam.rfid
    ORDER BY offspring_count DESC;
    """
    rows = connect(query)
    heads = ['Dam', '# of Offspring']
    return render_template('result.html', rows=rows, heads=heads)

# handle query POST and serve result web page
@app.route('/query_7', methods=['POST'])
# query function
def query_7():
    query = """
    SELECT a.sire, COUNT(*) as offspring_count
    FROM Animal a
    JOIN sessionanimaltrait s ON a.animal_id = s.animal_id
    WHERE s.trait_code = 357 -- BWT trait code
    AND CASE
      WHEN s.alpha_value ~ '^[+-]?[0-9]*\.?[0-9]+$' THEN s.alpha_value::numeric > 8.0
      ELSE FALSE
      END
    AND s.alpha_value IS NOT NULL
    AND (a.sire IS NOT NULL AND a.sire<> '')
    GROUP BY a.sire
    ORDER BY offspring_count DESC;
    """
    rows = connect(query)
    heads = ['Sire', '# of Offspring']
    return render_template('result.html', rows=rows, heads=heads)

@app.route('/query_8', methods=['POST'])
def query_8():
    query = """
    WITH BWTData AS (
    SELECT
        a.rfid,
        MAX(NULLIF(t.alpha_value, '')::NUMERIC) AS BirthWeight -- Using MAX to safely ignore NULLs
    FROM SessionAnimalTrait t
    JOIN Animal a ON t.animal_id = a.animal_id
    WHERE t.trait_code = 357 -- Birth weight trait code
      AND t.alpha_value <> '' -- Ensures that empty strings are not considered
    GROUP BY a.rfid
    ),
    WeaningWeights AS (
    SELECT
        a.rfid,
        ROUND(AVG(NULLIF(t.alpha_value, '')::NUMERIC), 1) AS AvgWeaningWeight
    FROM SessionAnimalTrait t
    JOIN Animal a ON t.animal_id = a.animal_id
    WHERE t.trait_code = 53 -- Live weight trait code
      AND EXTRACT(MONTH FROM t.when_measured) IN (7, 8, 9)
      AND EXTRACT(YEAR FROM t.when_measured) = EXTRACT(YEAR FROM a.dob)
      AND t.alpha_value <> '' -- Ensures that empty strings are not considered
    GROUP BY a.rfid
    HAVING ROUND(AVG(NULLIF(t.alpha_value, '')::NUMERIC), 1) > 0
    ),
    WinterWeights AS (
    SELECT
        a.rfid,
        ROUND(AVG(NULLIF(t.alpha_value, '')::NUMERIC), 1) AS AvgWinterWeight
    FROM SessionAnimalTrait t
    JOIN Animal a ON t.animal_id = a.animal_id
    WHERE t.trait_code = 53 -- Live weight trait code
      AND EXTRACT(MONTH FROM t.when_measured) IN (11, 12, 1)
      AND EXTRACT(YEAR FROM t.when_measured) = EXTRACT(YEAR FROM a.dob) + 1
      AND t.alpha_value <> '' -- Ensures that empty strings are not considered
    GROUP BY a.rfid
    HAVING ROUND(AVG(NULLIF(t.alpha_value, '')::NUMERIC), 1) > 0
    )
    SELECT 
    b.rfid,
    COALESCE(b.BirthWeight, 0) AS BirthWeight,
    COALESCE(wn.AvgWeaningWeight, 0) AS AvgWeaningWeight,
    COALESCE(w.AvgWinterWeight, 0) AS AvgWinterWeight
    FROM BWTData b
    LEFT JOIN WeaningWeights wn ON b.rfid = wn.rfid
    LEFT JOIN WinterWeights w ON b.rfid = w.rfid
    WHERE b.BirthWeight > 0 AND wn.AvgWeaningWeight > 0 AND w.AvgWinterWeight > 0
    ORDER BY b.rfid
    LIMIT 100;
    """
    rows = connect(query)  # The comma makes it a single 
    heads = ['Goat ID', 'Birth Weight' ,'AVG Weaning WT', 'AVG Winter WT']
    return render_template('result.html', rows=rows, heads=heads)

@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)
