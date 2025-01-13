/*
 * This file is part of Astarte.
 *
 * Copyright 2025 SECO Mind Srl
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
use mockall::mock;

pub type Streaming<T> = MockStreaming<T>;

mock! {
    pub Streaming<T: 'static> {
        pub async fn message(&mut self) -> Result<Option<T>, tonic::Status>;
    }
}

mock! {
    pub MessageHubClient<T: 'static> {
        pub fn with_interceptor<F>(
            inner: T,
            interceptor: F,
        ) -> MockMessageHubClient<tonic::service::interceptor::InterceptedService<T, F>>
        where
            F: 'static;

        pub async fn attach<R>(
            &mut self,
            request: R,
        ) -> std::result::Result<
            tonic::Response<Streaming<crate::MessageHubEvent>>,
            tonic::Status,
        >
        where
            R: tonic::IntoRequest<crate::Node> + 'static;

        pub async fn send<R>(
            &mut self,
            request: R,
        ) -> std::result::Result<tonic::Response<::pbjson_types::Empty>, tonic::Status>
        where
            R: tonic::IntoRequest<crate::AstarteMessage> + 'static;

        pub async fn detach<R>(
            &mut self,
            request: R,
        ) -> std::result::Result<tonic::Response<::pbjson_types::Empty>, tonic::Status>
        where
            R: tonic::IntoRequest<::pbjson_types::Empty> + 'static;

        pub async fn add_interfaces<R>(
            &mut self,
            request: R,
        ) -> std::result::Result<tonic::Response<::pbjson_types::Empty>, tonic::Status>
        where
            R: tonic::IntoRequest<crate::InterfacesJson> + 'static;

        pub async fn remove_interfaces<R>(
            &mut self,
            request: R,
        ) -> std::result::Result<tonic::Response<::pbjson_types::Empty>, tonic::Status>
        where
            R: tonic::IntoRequest<crate::InterfacesName> + 'static;

        pub async fn get_properties<R>(
            &mut self,
            request: R,
        ) -> std::result::Result<
            tonic::Response<crate::StoredProperties>,
            tonic::Status,
        >
        where
            R: tonic::IntoRequest<crate::InterfacesName> + 'static;

        pub async fn get_all_properties<R>(
            &mut self,
            request: R,
        ) -> std::result::Result<
            tonic::Response<crate::StoredProperties>,
            tonic::Status,
        >
        where
            R: tonic::IntoRequest<crate::StoredPropertiesFilter> + 'static;

        pub async fn get_property<R>(
            &mut self,
            request: R,
        ) -> std::result::Result<tonic::Response<crate::Property>, tonic::Status>
        where
            R: tonic::IntoRequest<crate::PropertyIdentifier> + 'static;
    }

    impl<T: 'static> std::clone::Clone for MessageHubClient<T> {
        fn clone(&self) -> Self;
    }
}
