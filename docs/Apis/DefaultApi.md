# DefaultApi

All URIs are relative to *http://time-to-planet-api.travisshears.xyz/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**planetPlanetGet**](DefaultApi.md#planetPlanetGet) | **GET** /planet/{planet} | Returns time in second to planet to send message to planet


<a name="planetPlanetGet"></a>
# **planetPlanetGet**
> inline_response_200 planetPlanetGet(planet)

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

