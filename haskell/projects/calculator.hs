module Main where
-- PROJECT: Pure Functional Calculator | runghc calculator.hs
-- Docs: https://www.haskell.org/

-- TODO 1 (Mini): getLine REPL, words to parse "3 + 4"
-- main :: IO ()
-- main = loop
--   where loop = do
--           putStr ">> "
--           line <- getLine
--           if line == "exit" then return ()
--           else do
--             case words line of
--               [a, op, b] -> case (reads a, reads b) of
--                 ([(x,"")] , [(y,"")]) -> case op of
--                   "+" -> print (x+y :: Double)
--                   "-" -> print (x-y)
--                   "*" -> print (x*y)
--                   "/" | y == 0    -> putStrLn "Error: division by zero"
--                       | otherwise -> print (x/y)
--                   _   -> putStrLn $ "Unknown operator: " ++ op
--                 _ -> putStrLn "Invalid numbers"
--               _ -> putStrLn "Usage: number op number"
--             loop

-- TODO 2 (Intermediate): Parser combinators
-- newtype Parser a = Parser { runParser :: String -> Maybe (a, String) }
-- instance Functor     Parser where ...
-- instance Applicative Parser where ...
-- instance Monad       Parser where ...
-- instance Alternative Parser where ...
--
-- charP :: Char -> Parser Char
-- digitP :: Parser Char
-- numberP :: Parser Double
-- opP :: Parser Char
--
-- -- Combine: exprP = termP `chainl1` addOp
-- -- where addOp = (+) <$ charP '+' <|> (-) <$ charP '-'
-- --       termP = factorP `chainl1` mulOp

-- TODO 3 (Advanced): AST with full evaluation
-- data Expr = Num Double
--           | BinOp Char Expr Expr
--           | Neg Expr
--           deriving (Show)
--
-- eval :: Expr -> Either String Double
-- eval (Num n)       = Right n
-- eval (Neg e)       = fmap negate (eval e)
-- eval (BinOp '+' a b) = (+) <$> eval a <*> eval b
-- eval (BinOp '-' a b) = (-) <$> eval a <*> eval b
-- eval (BinOp '*' a b) = (*) <$> eval a <*> eval b
-- eval (BinOp '/' a b) = do
--   bv <- eval b
--   if bv == 0 then Left "Division by zero" else fmap (/bv) (eval a)

main :: IO ()
main = putStrLn "TODO: implement calculator"
