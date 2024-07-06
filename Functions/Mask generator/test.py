
def annotate_images(json_path, base_image_directory, overlay_directory, Mask_directory):
    data = load_json_data(json_path)

    for dict1 in data:
        # DICTIONARY OF EACH IMAGE IS PASSED
        # we iterate through each dictionary (i.e. an element in the list)
        image_path = os.path.join(base_image_directory, dict1['data_title'])
        image = cv2.imread(image_path)

        #exception handeling
        if image is None:
            print(f"Image {dict['data_title']} not found.")
            continue
        if dict["label_status"] != "LABELLED":
            #if image is not labeled, continue to next image
            continue

        # Creating blank image
        blank_image = np.ones(image.shape, dtype=np.uint8) * 255  # White background

        for obj in dict["data_units"].values():
        # Extracting data_units{} > label{} > objects[]";1`"
        # data_units KAR K 1 KEY H JIS KI VALUE = DICTIONARY CONTAINING ALL THE ONTOLOGIES
        # VALUES OF ALL ONTOLOGIES IN IMAGE IS PASSED

            labels = obj["labels"] #this is the dict containing all the ontolgy (annotation & classification)

            # LIST OF ANNOTATIONS (ONLY) IS SELECTED
            # LIST OF ANNOTATIONS (ONLY) IS SELECTED
            annotaion_list = labels["objects"] #ONLY FOR ANNOTATIONS (not classification)




            # for overlay annotation
            # process_annotations(image,annotaion_list)
            # output_path = os.path.join(overlay_directory, dict['data_title'])
            # save_annotated_image(image, output_path)

            #for mask only annotation
            process_annotations(blank_image,annotaion_list)
            output_path = os.path.join(overlay_directory, dict['data_title'])
            save_annotated_image(blank_image, output_path)
