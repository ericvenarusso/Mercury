class MlTools:


    def map_target(data, column, target_dict):
        """
        Map a Data Frame target variable.
        
        Parameters
        ----------
        data : pd.DataFrame
            DataFrame object.
        
        column: string
            String that indentify the target column.

        target_dict: dict
            Dict with sources.
        """

        data[column] = data[column].apply(lambda x: target_dict[x])

        return data

    def separe_columns(data, columns, target):
        """
        Separe columns from a Dataframe in X, y.
        
        Parameters
        ----------
        data : pd.DataFrame
            DataFrame object.
        
        columns: list
            List that identifies the X columns.

        target: str
            String that identifies the y column.
        """

        X = data[columns]
        y = data[target]

        return  X, y