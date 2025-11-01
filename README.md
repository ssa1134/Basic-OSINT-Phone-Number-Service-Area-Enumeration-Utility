# Basic OSINT: Phone Number Service Area Enumeration Utility

A simple Python script designed for basic Open Source Intelligence (OSINT) gathering. It uses the `phonenumbers` library to parse a list of phone numbers and identify their associated service area or general geographical region (e.g., state or country).

This tool is intended for educational purposes to demonstrate basic reconnaissance techniques.

---

## ⚠️ Important Disclaimer: This is NOT a GPS Tracker

This tool **does not** provide real-time GPS location tracking.

The `phonenumbers` library's `geocoder` module only provides the **region where the phone number was originally registered** (e.g., "Punjab, India" or "Himachal Pradesh, India"). This information is static and based on the number's prefix (which maps to a specific telecom circle and service provider).

It **cannot** be used to find a device's current physical location. The comment `# LETS TRACK THE PHONE NUMBERS` in the original script is a misnomer; the correct term is **enumeration** or **geo-locating the service region**.

---

## 🚀 Setup & Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
    cd your-repository-name
    ```

2.  **Install the required library:**
    This script depends on the `phonenumbers` library.
    ```bash
    pip install phonenumbers
    ```

---

## 💻 How to Use

1.  **Edit the Script:**
    Open `Phone_Location.py` and modify the `phonenumbers.parse()` lines to include the numbers you wish to analyze. Ensure they are in E.164 format (e.g., `+CountryCodeNationalNumber`).

    ```python
    import phonenumbers
    from phonenumbers import geocoder

    # Add or change your target numbers here
    phone_number1 = phonenumbers.parse("+917009262789")
    phone_number2 = phonenumbers.parse("+918288933544")
    # ...add more as needed

    print("\nPhone Number Service Area Enumeration\n")
    print(geocoder.description_for_number(phone_number1, "en"))
    print(geocoder.description_for_number(phone_number2, "en"))
    ```

2.  **Run the script:**
    Execute the script from your terminal.
    ```bash
    python Phone_Location.py
    ```

---

## 📊 Example Output

Running the script as-is in the repository will produce the following output, identifying the *service circles* for the provided Indian numbers:
