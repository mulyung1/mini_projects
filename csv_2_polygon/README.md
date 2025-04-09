- Define additional_columns as a list of the required columns.

- Add each column to the layer's fields as QgsField with QVariant.String.

- Check that all required columns are present in the CSV.

- When setting the feature's attributes, include the values from the CSV row for the additional columns.

