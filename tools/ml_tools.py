class MlTools:


    def map_target(data, column, target_dict):
        data[column] = data[column].apply(lambda x: target_dict[x])
        return data