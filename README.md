# authorization-lambda-at-edge python using dynamodb

Code demonstrates authorization with Lambda@Edge along with Cloudfront and S3 static web pages 

# How to
1. Create S3 bucket with static website hosting feature
2. Create Cloudfront distribution with S3 bucket origin
3. Crete lambda function(python3.7) in N.Virginia Region
4. Configure Cloudfront Behaviour to trigger Viewer Request(Lambda Function Associations) and choose lambda function
5. Deploy lambda function to Lamba@Edge
6. Create dynamodb table and add items
