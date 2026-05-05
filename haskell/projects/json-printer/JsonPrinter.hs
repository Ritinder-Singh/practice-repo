module JsonPrinter where
-- PROJECT: Pure Functional JSON Pretty-Printer | runghc JsonPrinter.hs
import Data.List (intercalate)

-- TODO 1: JSON data type
-- data Json
--   = JNull
--   | JBool Bool
--   | JNumber Double
--   | JString String
--   | JArray [Json]
--   | JObject [(String, Json)]
--   deriving (Show, Eq)

-- TODO 2: Pretty printer with indentation
-- prettyPrint :: Json -> String
-- prettyPrint = pp 0
--   where
--     indent n = replicate (n * 2) ' '
--     pp _ JNull       = "null"
--     pp _ (JBool b)   = if b then "true" else "false"
--     pp _ (JNumber n) = if n == fromIntegral (round n) then show (round n :: Integer) else show n
--     pp _ (JString s) = "\"" ++ escapeStr s ++ "\""
--     pp n (JArray [])  = "[]"
--     pp n (JArray xs)  = "[\n" ++ intercalate ",\n" (map (\x -> indent (n+1) ++ pp (n+1) x) xs) ++ "\n" ++ indent n ++ "]"
--     pp n (JObject []) = "{}"
--     pp n (JObject pairs) = "{\n" ++ intercalate ",\n" (map (ppPair (n+1)) pairs) ++ "\n" ++ indent n ++ "}"
--     ppPair n (k, v) = indent n ++ "\"" ++ k ++ "\": " ++ pp n v
--     escapeStr = concatMap escChar
--     escChar '"'  = "\\\""
--     escChar '\\' = "\\\\"
--     escChar '\n' = "\\n"
--     escChar '\t' = "\\t"
--     escChar c    = [c]

-- TODO 3: JSON equality (structural)
-- jsonEq :: Json -> Json -> Bool
-- jsonEq JNull JNull = True
-- jsonEq (JBool a) (JBool b) = a == b
-- jsonEq (JNumber a) (JNumber b) = a == b
-- -- etc.

-- TODO 4: Mini parser (optional — use parser combinators from calculator exercise)
-- parseJson :: String -> Either String Json
-- -- parseJson s = runParser jsonP s >>= (\(v, rest) -> if null rest then Right v else Left "trailing input")

-- TODO 5: Test values
-- testValue :: Json
-- testValue = JObject
--   [ ("name", JString "Alice")
--   , ("age", JNumber 30)
--   , ("scores", JArray [JNumber 95, JNumber 87, JNumber 92])
--   , ("active", JBool True)
--   , ("address", JNull)
--   ]

main :: IO ()
main = putStrLn "TODO: implement JSON pretty-printer"
  -- Uncomment after implementation:
  -- putStrLn $ prettyPrint testValue
