from flask import Flask, render_template, request, jsonify, send_file
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/download')
def download_file():
    file_path = "zoho_email_responses.xlsx"  # Ensure this file is correctly generated
    return send_file(file_path, as_attachment=True)    

@app.route('/run-script', methods=['POST'])
def run_script():
    try:
        # Run the script
        result = subprocess.run(['python', 'logic.py'], capture_output=True, text=True, check=True)
        
        return jsonify({'output': result.stdout})
    
    except subprocess.CalledProcessError as e:
        return jsonify({'error': e.stderr}), 500

if __name__ == '__main__':
    app.run(debug=True)
