import streamlit as st

from generate_set import generate_sets


st.title("Sythetic Spatial Data Generation")


# USER INPUTS
card = st.number_input("Enter the number of polygons", 1, 100000, 36)
xsize = st.number_input("Enter the xsize", 1, 100000, 500)
ysize = st.number_input("Enter the ysize", 1, 100000, 500)
vertices_bounds = st.slider("Enter the range of vertices", 3, 10, (3, 7))
irregularity_clip = st.slider(
    "Enter the range of irregularity", 0.0, 1.0, (0.0, 0.8))
spikiness_clip = st.slider(
    "Enter the range of spikiness", 0.0, 1.0, (0.0, 0.8))
show_grid = st.checkbox("Show Grid", value=True)


# Visualize the generated polygons
Image = generate_sets(card, xsize, ysize, vertices_bounds, show_grid,
                      irregularity_clip=irregularity_clip[1], spikiness_clip=spikiness_clip[1])
st.image(image=Image, caption='Polygon Generation')


# Download the generated polygons as CSV
with open('my_file_csv.csv') as f:
    st.download_button('Download CSV', f, mime='text/csv')

# Download the generated polygons as Shapefile
# with open('my_file_shape.shp', 'rb') as f:
#     st.download_button('Download Shapefile', f,
#                        mime='application/octet-stream')
