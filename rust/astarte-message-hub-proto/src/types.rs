/*
 * This file is part of Astarte.
 *
 * Copyright 2022 SECO Mind Srl
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

use std::collections::HashMap;

use chrono::{DateTime, Utc};

use crate::{
    proto_message_hub::astarte_data::AstarteData, AstarteDatastreamInidividual,
    AstarteDatastreamObject, AstarteDateTimeArray,
};

/// This macro can be used to implement the from trait for an AstarteDataTypeIndividual from a
/// generic type that is not an array.
macro_rules! from_to_impl {
    ($from:ty, $to:path) => {
        impl From<$from> for crate::proto_message_hub::astarte_data::AstarteData {
            fn from(value: $from) -> Self {
                $to(value.into())
            }
        }
    };
    ($from:ty, $array:ident, $to:path) => {
        impl From<$from> for crate::proto_message_hub::astarte_data::AstarteData {
            fn from(value: $from) -> Self {
                let value = crate::proto_message_hub::$array {
                    values: value.into(),
                };

                $to(value)
            }
        }
    };
}

from_to_impl!(f64, AstarteData::Double);
from_to_impl!(f32, AstarteData::Double);
from_to_impl!(i32, AstarteData::Integer);
from_to_impl!(bool, AstarteData::Boolean);
from_to_impl!(i64, AstarteData::LongInteger);
from_to_impl!(&str, AstarteData::String);
from_to_impl!(String, AstarteData::String);
from_to_impl!(&String, AstarteData::String);
from_to_impl!(Vec<u8>, AstarteData::BinaryBlob);
from_to_impl!(&[u8], AstarteData::BinaryBlob);
from_to_impl!(DateTime<Utc>, AstarteData::DateTime);
from_to_impl!(Vec<f64>, AstarteDoubleArray, AstarteData::DoubleArray);
from_to_impl!(&[f64], AstarteDoubleArray, AstarteData::DoubleArray);
from_to_impl!(Vec<i32>, AstarteIntegerArray, AstarteData::IntegerArray);
from_to_impl!(&[i32], AstarteIntegerArray, AstarteData::IntegerArray);
from_to_impl!(Vec<bool>, AstarteBooleanArray, AstarteData::BooleanArray);
from_to_impl!(&[bool], AstarteBooleanArray, AstarteData::BooleanArray);
from_to_impl!(
    Vec<i64>,
    AstarteLongIntegerArray,
    AstarteData::LongIntegerArray
);
from_to_impl!(
    &[i64],
    AstarteLongIntegerArray,
    AstarteData::LongIntegerArray
);
from_to_impl!(Vec<String>, AstarteStringArray, AstarteData::StringArray);
from_to_impl!(&[String], AstarteStringArray, AstarteData::StringArray);
from_to_impl!(
    Vec<Vec<u8>>,
    AstarteBinaryBlobArray,
    AstarteData::BinaryBlobArray
);

impl From<Vec<DateTime<Utc>>> for AstarteData {
    fn from(value: Vec<DateTime<Utc>>) -> Self {
        let values = value
            .into_iter()
            .map(pbjson_types::Timestamp::from)
            .collect();

        AstarteData::DateTimeArray(AstarteDateTimeArray { values })
    }
}

impl<T> From<T> for AstarteDatastreamInidividual
where
    T: Into<AstarteData>,
{
    fn from(value: T) -> Self {
        Self {
            data: Some(crate::proto_message_hub::AstarteData {
                astarte_data: Some(value.into()),
            }),
        }
    }
}

impl From<HashMap<String, AstarteData>> for AstarteDatastreamObject {
    fn from(value: HashMap<String, AstarteData>) -> Self {
        let data = value
            .into_iter()
            .map(|(k, v)| {
                (
                    k,
                    crate::AstarteData {
                        astarte_data: Some(v),
                    },
                )
            })
            .collect();

        AstarteDatastreamObject { data }
    }
}
impl From<HashMap<String, crate::AstarteData>> for AstarteDatastreamObject {
    fn from(value: HashMap<String, crate::AstarteData>) -> Self {
        AstarteDatastreamObject { data: value }
    }
}

#[cfg(test)]
mod test {
    use std::collections::HashMap;

    use chrono::DateTime;

    use super::*;
    use crate::proto_message_hub;

    #[test]
    fn from_double_to_astarte_individual_type_success() {
        let expected_double_value: f64 = 15.5;
        let value = AstarteDatastreamInidividual::from(expected_double_value)
            .data
            .unwrap()
            .astarte_data
            .unwrap();

        assert_eq!(AstarteData::Double(expected_double_value), value);
    }

    #[test]
    fn from_integer_into_astarte_individual_type_success() {
        let expected: i32 = 15;
        let value = AstarteDatastreamInidividual::from(expected)
            .data
            .unwrap()
            .astarte_data
            .unwrap();

        assert_eq!(AstarteData::Integer(expected), value);
    }

    #[test]
    fn bool_into_astarte_individual_type_success() {
        let expected = true;
        let value = AstarteDatastreamInidividual::from(expected)
            .data
            .unwrap()
            .astarte_data
            .unwrap();

        assert_eq!(AstarteData::Boolean(expected), value);
    }

    #[test]
    fn u8_array_into_individual_type_success() {
        let expected: Vec<u8> = vec![10, 44];
        let value = AstarteDatastreamInidividual::from(expected.clone())
            .data
            .unwrap()
            .astarte_data
            .unwrap();

        assert_eq!(AstarteData::BinaryBlob(expected), value);
    }

    #[test]
    fn double_array_into_individual_type_success() {
        let expected: Vec<f64> = vec![10.54, 44.99];
        let value = AstarteDatastreamInidividual::from(expected.clone())
            .data
            .unwrap()
            .astarte_data
            .unwrap();

        assert_eq!(
            AstarteData::DoubleArray(proto_message_hub::AstarteDoubleArray { values: expected }),
            value
        );
    }

    #[test]
    fn string_array_into_individual_type_success() {
        let expected: Vec<String> = vec!["test1".to_owned(), "test2".to_owned()];
        let value = AstarteDatastreamInidividual::from(expected.clone())
            .data
            .unwrap()
            .astarte_data
            .unwrap();

        assert_eq!(
            AstarteData::StringArray(proto_message_hub::AstarteStringArray { values: expected }),
            value
        );
    }

    #[test]
    fn double_into_astarte_data_type_success() {
        let expected: f32 = 15.5;
        let value = AstarteDatastreamInidividual::from(expected)
            .data
            .unwrap()
            .astarte_data
            .unwrap();

        assert_eq!(AstarteData::Double(expected.into()), value);
    }

    #[test]
    fn longinteger_into_astarte_data_type_success() {
        let expected: i64 = 15;
        let value = AstarteDatastreamInidividual::from(expected)
            .data
            .unwrap()
            .astarte_data
            .unwrap();

        assert_eq!(AstarteData::LongInteger(expected), value);
    }

    #[test]
    fn string_into_astarte_data_type_success() {
        let expected: String = "15".to_owned();
        let value = AstarteDatastreamInidividual::from(expected.clone())
            .data
            .unwrap()
            .astarte_data
            .unwrap();

        assert_eq!(AstarteData::String(expected), value);
    }

    #[test]
    fn datetime_into_astarte_data_type_success() {
        let expected = Utc::now();

        let value = AstarteDatastreamInidividual::from(expected)
            .data
            .unwrap()
            .astarte_data
            .unwrap();

        if let AstarteData::DateTime(date_time_value) = value {
            let resul_date_time: DateTime<Utc> = date_time_value.try_into().unwrap();
            assert_eq!(expected, resul_date_time);
        } else {
            panic!();
        }
    }

    #[test]
    fn double_array_into_astarte_data_type_success() {
        let expected: Vec<f64> = vec![10.54, 44.99];
        let value = AstarteDatastreamInidividual::from(expected.clone())
            .data
            .unwrap()
            .astarte_data
            .unwrap();

        assert_eq!(
            AstarteData::DoubleArray(proto_message_hub::AstarteDoubleArray { values: expected }),
            value
        );
    }

    #[test]
    fn integer_array_into_astarte_data_type_success() {
        let expected: Vec<i32> = vec![10, 44];
        let value = AstarteDatastreamInidividual::from(expected.clone())
            .data
            .unwrap()
            .astarte_data
            .unwrap();

        assert_eq!(
            AstarteData::IntegerArray(proto_message_hub::AstarteIntegerArray { values: expected }),
            value
        );
    }

    #[test]
    fn long_integer_array_into_astarte_data_type_success() {
        let expected: Vec<i64> = vec![10, 44];
        let value = AstarteDatastreamInidividual::from(expected.clone())
            .data
            .unwrap()
            .astarte_data
            .unwrap();

        assert_eq!(
            AstarteData::LongIntegerArray(proto_message_hub::AstarteLongIntegerArray {
                values: expected
            }),
            value
        );
    }

    #[test]
    fn bool_array_into_astarte_data_type_success() {
        let expected: Vec<bool> = vec![false, true];
        let value = AstarteDatastreamInidividual::from(expected.clone())
            .data
            .unwrap()
            .astarte_data
            .unwrap();

        assert_eq!(
            AstarteData::BooleanArray(proto_message_hub::AstarteBooleanArray { values: expected }),
            value
        );
    }

    #[test]
    fn string_array_into_astarte_data_type_success() {
        let expected: Vec<String> = vec!["test1".to_owned(), "test2".to_owned()];
        let value = AstarteDatastreamInidividual::from(expected.clone())
            .data
            .unwrap()
            .astarte_data
            .unwrap();

        assert_eq!(
            AstarteData::StringArray(proto_message_hub::AstarteStringArray { values: expected }),
            value
        );
    }

    #[test]
    fn binary_blob_array_into_astarte_data_type_success() {
        let expected: Vec<Vec<u8>> = vec![vec![12, 245], vec![78, 11, 128]];
        let value = AstarteDatastreamInidividual::from(expected.clone())
            .data
            .unwrap()
            .astarte_data
            .unwrap();

        assert_eq!(
            AstarteData::BinaryBlobArray(proto_message_hub::AstarteBinaryBlobArray {
                values: expected
            }),
            value
        );
    }

    #[test]
    fn datetime_array_into_astarte_type_individual_success() {
        let expected = vec![Utc::now(), Utc::now()];
        let value = AstarteDatastreamInidividual::from(expected.clone())
            .data
            .unwrap()
            .astarte_data
            .unwrap();

        let AstarteData::DateTimeArray(value) = value else {
            panic!();
        };

        assert_eq!(value.values.len(), expected.len());

        for (value, exp) in value.values.into_iter().zip(expected) {
            let date_time = DateTime::<Utc>::try_from(value).unwrap();

            assert_eq!(date_time, exp);
        }
    }

    #[test]
    fn map_into_astarte_data_type_success() {
        let expected_i32 = 5;
        let expected_f64 = 5.12;
        let mut map_val: HashMap<String, AstarteData> = HashMap::new();
        map_val.insert("i32".to_owned(), expected_i32.into());
        map_val.insert("f64".to_owned(), expected_f64.into());

        let astarte_data_object: AstarteDatastreamObject = map_val.into();

        let mut data = astarte_data_object.data;

        let i32_value = data
            .remove("i32")
            .and_then(|data| data.astarte_data)
            .unwrap();

        assert_eq!(AstarteData::Integer(expected_i32), i32_value);

        let f64_value = data
            .remove("f64")
            .and_then(|data| data.astarte_data)
            .unwrap();

        assert_eq!(AstarteData::Double(expected_f64), f64_value);
    }
}
