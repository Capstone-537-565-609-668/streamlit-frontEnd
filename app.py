import streamlit as st
import random
from generate_set import generate_sets
from generate_polygon import generate_polygon
from PIL import Image,  ImageDraw

route = st.sidebar.selectbox(
    'Select a route',
    ('Generate Spatial Data', 'Generate Park Data')
)

if(route == 'Generate Spatial Data'):
    # USER INPUTS
    st.title("Sythetic Spatial Data Generation")
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

else:
    st.title("Generating data for Park")
    data_df_describe = {
        "num_vertices": {
            'mean': 8.14,
            'min': 4,
            'max': 70
        },
        "irregularity": {
            "mean": 0.635194,
            'min': 0.084276,
            'max': 0.998559
        },
        'spikiness':
        {
            "mean": 0.525993,
            'min': 0.250000,
            'max': 0.946429
        },
        'avg_radius':
        {
            'mean': 0.000101,
            'min': 0.000006,
            'max': 0.001699
        }
    }

    vertices = generate_polygon((250, 250),
                                data_df_describe["avg_radius"]["max"] *
                                60000,

                                random.uniform(
                                    data_df_describe["irregularity"]["min"], data_df_describe["irregularity"]["max"]),
                                random.uniform(
                                    data_df_describe["spikiness"]["min"], data_df_describe["spikiness"]["max"]),
                                data_df_describe["num_vertices"]["min"])
    # random.randint(data_df_describe["num_vertices"]["min"], data_df_describe["num_vertices"]["max"]))

    black = (0, 0, 0)
    white = (255, 255, 255)
    img = Image.new('RGB', (500, 500), white)
    im_px_access = img.load()
    draw = ImageDraw.Draw(img)

    # either use .polygon(), if you want to fill the area with a solid colour
    draw.polygon(vertices, outline=black, fill=white)

    draw.line(vertices + [vertices[0]], width=2, fill=black)
    st.image(image=img, caption='whatever')


# Download the generated polygons as Shapefile
# with open('my_file_shape.shp', 'rb') as f:
#     st.download_button('Download Shapefile', f,
#                        mime='application/octet-stream')
