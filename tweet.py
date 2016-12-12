import tweepy
import twkey

CS = twkey.CS
CK = twkey.CK
AT = twkey.AT
AS = twkey.AS

auth = tweepy.OAuthHandler(CK,CS)
auth.set_access_token(AT,AS)


#text = "hogehoge"
api = tweepy.API(auth)
api.update_status("hogehoge")
