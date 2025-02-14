# Impact of 2015 Wildfires on Air Quality in Washington

## Author & Course Information  
**David Melesse**  
**Westmont College**  
**CS - 150 Data Visualization for Community Action**  

## Thesis Statement  
Wildfires have a significant impact on air quality and public health. By analyzing PM2.5 concentration levels before, during, and after major wildfires in Washington state in 2015, this visualization highlights the relationship between wildfire activity and air pollution, advocating for increased wildfire prevention and mitigation efforts.

## Context for the Data Visualization  
Wildfires in Washington have grown in frequency and intensity, leading to severe air pollution that affects millions of residents. PM2.5, a key air pollutant, can cause respiratory and cardiovascular issues. This project visualizes PM2.5 levels across different counties and compares them with wildfire data to reveal patterns and encourage action in wildfire prevention.

## Data Sources  
- **EPA PM2.5 Data**: Provides daily mean PM2.5 concentration levels across different counties in Washington for 2015.  
- **Washington Large Wildfires Dataset (1973-2022)**: Includes information on wildfire events, specifically focusing on the number of acres burned in 2015.  

## Visualization Strategy  
Using **Dash and Plotly**, the interactive dashboard presents two key visualizations:
- **Line Chart**: Displays PM2.5 concentration over time for different counties, allowing users to observe trends and fluctuations.
- **Bar Chart**: Illustrates the total acres burned by wildfires on specific dates in 2015, linking wildfire events to spikes in air pollution.

## Strategies from "Storytelling with Data" (SwD)  
To ensure clarity and engagement, the following SwD principles are applied:
- **Contextual Framing**: The dashboard includes a clear title and labels to set the stage for viewers.
- **Interactive Exploration**: A dropdown filter enables users to explore county-specific data, making the visualization more relevant to different regions.
- **Visual Simplicity**: The charts use clean, intuitive designs with appropriate colors and axis labels to highlight key insights.
- **Narrative Flow**: The combination of PM2.5 trends and wildfire data helps tell a compelling story about the environmental impact of wildfires.

## Call to Action  
This project aims to raise awareness about the consequences of wildfires on air quality and public health. By understanding these patterns, policymakers and communities can advocate for better wildfire prevention measures, stricter environmental policies, and proactive air quality management.

---

## How to Run the Project  
1. Install dependencies:  
   ```bash
   pip install dash pandas plotly
   ```  
2. Run the application:  
   ```bash
   python app.py
   ```  
3. Open the browser and interact with the dashboard to explore air quality trends in Washington.





