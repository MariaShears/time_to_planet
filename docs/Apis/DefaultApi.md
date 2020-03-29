# DefaultApi

All URIs are relative to *http://time-to-planet-api.travisshears.xyz/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDuration**](DefaultApi.md#getDuration) | **GET** /planet/{planet} | Returns time in second to planet to send message to planet


<a name="getDuration"></a>
# **getDuration**
> inline_response_200 getDuration(planet)

Returns time in second to planet to send message to planet

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **planet** | **String**| planet -- mars, venus, jupiter | [default to null]

### Return type

[**inline_response_200**](..//Models/inline_response_200.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

