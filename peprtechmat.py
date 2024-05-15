# Import necessary libraries
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Streamlit app
def main():
    st.set_page_config(page_title='SRE Maturity Progression', page_icon='📈', layout='wide')
    st.title("SRE Maturity Progression Visualization")

    # Use columns to organize the layout
    col1, col2 = st.columns(2)

    with col1:
        # User input: Organization's aim with a placeholder
        organization_aim = st.text_input("Enter your organization's aim:", "Improve system reliability")

        # Display the organization's aim with markdown for better formatting
        st.markdown(f"**Organization's Aim:** {organization_aim}")

        # Simulate the interaction between people, processes, and technology with better labeling
        people = st.slider("People (1-5)", 1, 5, 3, help='Rate the involvement of people in SRE practices.')
        processes = st.slider("Processes (1-5)", 1, 5, 3, help='Rate the maturity of processes in your SRE practices.')
        technology = st.slider("Technology (1-5)", 1, 5, 5, help='Rate the adoption of technology in your SRE practices.')

    with col2:
        # Create the plot
        fig, ax = plt.subplots()

        # Define the origin
        origin = np.array([0, 0])

        # Define vectors for People, Processes, and Technology
        people_vector = np.array([people, 0])
        processes_vector = np.array([processes * np.cos(np.pi/3), processes * np.sin(np.pi/3)])
        technology_vector = np.array([technology * np.cos(-np.pi/3), technology * np.sin(-np.pi/3)])

        # Draw the vectors
        ax.quiver(*origin, *people_vector, scale=1, scale_units='xy', angles='xy', color='red', label='People')
        ax.quiver(*origin, *processes_vector, scale=1, scale_units='xy', angles='xy', color='blue', label='Processes')
        ax.quiver(*origin, *technology_vector, scale=1, scale_units='xy', angles='xy', color='green', label='Technology')

        # Calculate the angles between the vectors
        angle_people_processes = np.arccos(np.dot(people_vector, processes_vector) / (np.linalg.norm(people_vector) * np.linalg.norm(processes_vector)))
        angle_processes_technology = np.arccos(np.dot(processes_vector, technology_vector) / (np.linalg.norm(processes_vector) * np.linalg.norm(technology_vector)))
        angle_technology_people = np.arccos(np.dot(technology_vector, people_vector) / (np.linalg.norm(technology_vector) * np.linalg.norm(people_vector)))

        # Annotate the angles
        ax.annotate(f'{np.degrees(angle_people_processes):.2f}°', xy=(people/2, people/8), color='purple')
        ax.annotate(f'{np.degrees(angle_processes_technology):.2f}°', xy=(processes/2 * np.cos(np.pi/6), processes/2 * np.sin(np.pi/6)), color='purple')
        ax.annotate(f'{np.degrees(angle_technology_people):.2f}°', xy=(technology/2 * np.cos(-np.pi/6), technology/2 * np.sin(-np.pi/6)), color='purple')

        # Calculate the resultant vector
        resultant_vector = people_vector + processes_vector + technology_vector

        # Draw the resultant vector
        ax.quiver(*origin, *resultant_vector, scale=1, scale_units='xy', angles='xy', color='black', label='Resultant Vector', linewidth=2)

        # Determine the dominant factor driving the resultant vector
        dominant_factor = max(people, processes, technology)
        if dominant_factor == people:
            driven_by = 'People'
        elif dominant_factor == processes:
            driven_by = 'Processes'
        else:
            driven_by = 'Technology'

        # Annotate the resultant vector
        ax.text(*resultant_vector, f'  Resultant Vector (Driven by {driven_by})', color='black')

        # Set the aspect of the plot to be equal
        ax.set_aspect('equal')

        # Set the limits of the plot
        max_value = max(people, processes, technology)
        ax.set_xlim(-1, max_value + 1)
        ax.set_ylim(-max_value - 1, max_value + 1)

        # Add a legend
        ax.legend()

        # Display the plot in the Streamlit app
        st.pyplot(fig)

if __name__ == "__main__":
    main()
