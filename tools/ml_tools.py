class MlTools:


    def map_target(data, column, target_dict):
        """
        Map a Data Frame target variable.
        
        Parameters
        ----------
        data : pd.DataFrame
            DataFrame object
        
        column: string
            String that indentify the target column.

        target_dict: dict
            Dict with sources.
        """

        data[column] = data[column].apply(lambda x: target_dict[x])

        return data