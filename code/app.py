# app.py

import streamlit as st

# Define the main function for the Streamlit app
def main():
    st.title("Satellite Threat Modeling")

    # Step 1: Define the Scope
    st.header("1. Define the Scope")
    satellite_system = st.text_input("Describe the satellite system:")

    # Step 2: Identify Threats
    st.header("2. Identify Threats")
    threats = st.text_area("List potential threats (one per line):").split('\n')

    # Step 3: Assess Vulnerabilities
    st.header("3. Assess Vulnerabilities")
    vulnerabilities = st.text_area("List vulnerabilities (one per line):").split('\n')

    # Step 4: Mitigate Risks
    st.header("4. Mitigate Risks")
    mitigations = st.text_area("List mitigation strategies (one per line):").split('\n')

    # Step 5: Visualize & Report
    st.header("5. Visualize & Report")
    if st.button("Generate Report"):
        st.subheader("Threats")
        for threat in threats:
            st.write("- ", threat)
        
        st.subheader("Vulnerabilities")
        for vulnerability in vulnerabilities:
            st.write("- ", vulnerability)
        
        st.subheader("Mitigation Strategies")
        for mitigation in mitigations:
            st.write("- ", mitigation)

if __name__ == "__main__":
    main()
