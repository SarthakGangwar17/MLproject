import sys
import numpy as np
import pandas as pd
from dataclasses import  dataclass
from sklearn.preprocessing import OneHotEncoder ,StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from source.utils import save_object 
from source.exception import customException
from source.Logging import logging
from sklearn.compose import ColumnTransformer
import os


@dataclass
class dataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts',"preprocessor.pkl")



class dataTransformation:
    def __init__(self):
        self.data_transformation_config=dataTransformationConfig()

    def get_data_transformer_obj(self):
        try:
            numerical_column=['reading score', 'writing score']
            categorical_column=['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course']
            
            num_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="median")),
                    ("Scaler",StandardScaler())
                ]
            )
            logging.info("Standard Scaling is completed")
            cat_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="most_frequent")),
                    ("Onehotiencoder",OneHotEncoder()),
                    ("Scaler",StandardScaler(with_mean=False))

                ]
            )
            logging.info("Categorical column encoding completed")

            preprocessor=ColumnTransformer(
                [
                    ("numerical pipline",num_pipeline,numerical_column),
                    ("categorical pipeline",cat_pipeline,categorical_column)

                ]
            )
            return preprocessor
            logging.info("column transformation has done")
        except Exception as e:
            raise customException(e,sys)
        
    logging.info("Initiating data transformation .")

    def initiate_data_transformation(self,train_data_path,test_data_path):
        try:

            traindf=pd.read_csv(train_data_path)
            testdf=pd.read_csv(test_data_path)
            logging.info("Read train and test data")
            preprocessor_obj=self.get_data_transformer_obj()
            target_column_name="math score"
            numerical_column=["reading score","writing score"]
            input_feature_train_df=traindf.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=traindf[target_column_name]

            input_feature_test_df=testdf.drop(columns=[target_column_name])
            target_feature_test_df=testdf[target_column_name]

            input_feature_train_arr=preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessor_obj.transform(input_feature_test_df)

            trainarr=np.c_[
            input_feature_train_arr,np.array(target_feature_train_df)
            ]
            testarr=np.c_[
            input_feature_test_arr,np.array(target_feature_test_df)
            ]
        
            logging.info("saved preprocessing objects.")

            save_object(
            file_path=self.data_transformation_config.preprocessor_obj_file_path,
            obj=preprocessor_obj
            )

            return(
            trainarr,
            testarr,
            self.data_transformation_config.preprocessor_obj_file_path
            )

        except Exception as e:
            raise customException(e,sys)
            

            

