import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def draw_coherent_MUS_plot(n=4):

    R = n

    fig = plt.figure()
    ax = fig.add_subplot(2,1,1)
    ax.axis("equal")
    ax.set_ylim(ymin=0.0, ymax=np.sqrt(n)+n)
    ax.set_xlim(xmin=0.0, xmax=np.sqrt(n)+n)
    plt.xlim(xmin=0.0)

    # Plotting the Classical State
    y0 = np.sqrt(16*R**2/17)
    x0 = y0/4
    #ax.quiver(0,0,x0,y0)
    ax.arrow(0,0,x0,y0, fc="k", ec="k", head_width=0.1, head_length=0.1)
    classical_state = plt.Circle((x0,y0), radius=0.25, color='r')
    ax.add_patch(classical_state)
    ax.annotate('Classical State', xy=(x0,y0), xytext=(x0,y0+0.5))

    # Plot Coherent State MUS
    (x1, y1) = (np.sqrt(R**2/2), np.sqrt(R**2/2))
    #ax.quiver(0, 0, x1, y1)
    ax.arrow(0,0,x1,y1, fc="k", ec="k", head_width=0.1, head_length=0.1)
    coherent_state = patches.Circle((x1,y1), radius=np.sqrt(n)/2, color='y')
    ax.add_patch(coherent_state)
    ax.annotate('Coherent State', xy=(x1,y1), xytext=(x1+np.sqrt(n)/2,y1+np.sqrt(n)/2))

    # Determine coordinates for dashed lines that are tangent
    # to coherent MUS
    deg0 = np.arcsin((np.sqrt(R)/2)/R)
    deg_radial_to_horizontal = np.arcsin(y1/R)
    deg1 = deg_radial_to_horizontal - deg0
    hypot = np.sqrt(R**2 + (np.sqrt(R)/2)**2)
    x_bottom_dash = hypot * np.cos(deg1)
    y_bottom_dash = hypot * np.sin(deg1)
    slope = y_bottom_dash / x_bottom_dash
    x_btm_dashed_coords = 1.5*np.linspace(0, x_bottom_dash, 10)
    y_btm_dashed_coords = slope * x_btm_dashed_coords
    plt.plot(x_btm_dashed_coords, y_btm_dashed_coords, linestyle='--', marker="None", color="b")

    # Top dashed line
    deg2 = deg_radial_to_horizontal + deg0
    x_top_dash = hypot * np.cos(deg2)
    y_top_dash = hypot * np.sin(deg2)
    slope = y_top_dash / x_top_dash
    x_top_dash_coords = 1.5*np.linspace(0, x_top_dash, 10)
    y_top_dash_coords = slope * x_top_dash_coords
    plt.plot(x_top_dash_coords, y_top_dash_coords, linestyle='--', marker="None", color="b")

    # Dashed line perpendicular to radial, tangential to point of circle closest to origin
    hypot_to_circ_btm = hypot - np.sqrt(n)/2
    y_btm_perp = hypot_to_circ_btm * np.sin(deg_radial_to_horizontal)
    x_btm_perp = hypot_to_circ_btm * np.cos(deg_radial_to_horizontal)
    perp_slope = -1
    x_btm_perp_coords = np.linspace(x_btm_perp - np.sqrt(n)/2, x_btm_perp + np.sqrt(n)/2, 10)
    b_btm = get_intercept(x_btm_perp, y_btm_perp, perp_slope)
    y_btm_perp_coords = perp_slope * x_btm_perp_coords + b_btm
    plt.plot(x_btm_perp_coords, y_btm_perp_coords, linestyle='--', marker="None", color="b")

    # Dashed line perpendicular to radial, tangential to point of circle furthest to origin
    hypot_to_circ_top = hypot + np.sqrt(n)/2
    y_top_perp = hypot_to_circ_top * np.sin(deg_radial_to_horizontal)
    x_top_perp = hypot_to_circ_top * np.cos(deg_radial_to_horizontal)
    x_top_perp_coords = np.linspace(x_top_perp - np.sqrt(n)/1.5, x_top_perp + np.sqrt(n)/1.5, 10)
    b_top = get_intercept(x_top_perp, y_top_perp, perp_slope)
    y_top_perp_coords = perp_slope * x_top_perp_coords + b_top
    plt.plot(x_top_perp_coords, y_top_perp_coords, linestyle='--', marker="None", color="b")

    # Plot squeezed state MUS
    x2 = y0
    y2 = x0
    angle_of_rotation = (180/np.pi)*np.arctan(y2/x2)
    #ax.quiver(0, 0, x2, y2)
    ax.arrow(0,0,x2,y2, fc="k", ec="k", head_width=0.1, head_length=0.1)
    squeezed_state = patches.Ellipse((x2, y2), n, 1, color='g', angle=angle_of_rotation)
    ax.add_patch(squeezed_state)
    ax.annotate('Squeezed State', xy=(x2,y2), xytext=(x2,y2-R/4))

    # Determine coordinates for dashed lines that are tangent
    # to squeezed MUS
    deg0_sqz = np.arcsin((1/2)/R)
    deg_radial_to_horizontal_sqz = np.arcsin(y2/R)
    deg1_sqz = deg_radial_to_horizontal_sqz - deg0_sqz
    hypot_sqz = np.sqrt(R**2 + (np.sqrt(R)/2)**2)
    x_bottom_dash_sqz = hypot_sqz * np.cos(deg1_sqz)
    y_bottom_dash_sqz = hypot_sqz * np.sin(deg1_sqz)
    slope_sqz = y_bottom_dash_sqz / x_bottom_dash_sqz
    x_btm_dashed_coords_sqz = 2*np.linspace(0, x_bottom_dash_sqz, 10)
    y_btm_dashed_coords_sqz = slope_sqz * x_btm_dashed_coords_sqz
    plt.plot(x_btm_dashed_coords_sqz, y_btm_dashed_coords_sqz, linestyle='--', marker="None", color="b")

    # Top dashed line
    deg2_sqz = deg_radial_to_horizontal_sqz + deg0_sqz
    x_top_dash_sqz = hypot_sqz * np.cos(deg2_sqz)
    y_top_dash_sqz = hypot_sqz * np.sin(deg2_sqz)
    slope_sqz = y_top_dash_sqz / x_top_dash_sqz
    x_top_dash_coords_sqz = 2*np.linspace(0, x_top_dash_sqz, 10)
    y_top_dash_coords_sqz = slope_sqz * x_top_dash_coords_sqz
    plt.plot(x_top_dash_coords_sqz, y_top_dash_coords_sqz, linestyle='--', marker="None", color="b")

    # Dashed line perpendicular to radial, tangential to point of squeezed state closest to origin
    hypot_to_sqz_btm = hypot_sqz - n/2
    y_btm_perp_sqz = hypot_to_sqz_btm * np.sin(deg_radial_to_horizontal_sqz)
    x_btm_perp_sqz = hypot_to_sqz_btm * np.cos(deg_radial_to_horizontal_sqz)
    perp_slope_sqz = -x2/y2
    x_btm_perp_coords_sqz = np.linspace(x_btm_perp_sqz - np.sqrt(n)/5, x_btm_perp_sqz + np.sqrt(n)/5, 10)
    b_btm_sqz = get_intercept(x_btm_perp_sqz, y_btm_perp_sqz, perp_slope_sqz)
    y_btm_perp_coords_sqz = perp_slope_sqz * x_btm_perp_coords_sqz + b_btm_sqz
    plt.plot(x_btm_perp_coords_sqz, y_btm_perp_coords_sqz, linestyle='--', marker="None", color="b")

    # Dashed line perpendicular to radial, tangential to point of circle furthest to origin
    hypot_to_sqz_top = hypot_sqz + n/2
    y_top_perp_sqz = hypot_to_sqz_top * np.sin(deg_radial_to_horizontal_sqz)
    x_top_perp_sqz = hypot_to_sqz_top * np.cos(deg_radial_to_horizontal_sqz)
    x_top_perp_coords_sqz = np.linspace(x_top_perp_sqz - np.sqrt(n)/4, x_top_perp_sqz + np.sqrt(n)/4, 10)
    b_top_sqz = get_intercept(x_top_perp_sqz, y_top_perp_sqz, perp_slope_sqz)
    y_top_perp_coords_sqz = perp_slope_sqz * x_top_perp_coords_sqz + b_top_sqz
    plt.plot(x_top_perp_coords_sqz, y_top_perp_coords_sqz, linestyle='--', marker="None", color="b")

    origin = (0,0)
    x_r = 16
    x_y=16

    plt.show()

def get_intercept(x, y, m):
    return y - (m * x)

if __name__ == '__main__':
    draw_coherent_MUS_plot()
