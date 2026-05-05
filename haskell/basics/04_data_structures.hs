-- TOPIC: Data Structures | ghci: :load 04_data_structures.hs
-- import qualified Data.Map.Strict as Map
-- import qualified Data.Set as Set
-- import qualified Data.Sequence as Seq

-- TODO 1: Data.Map.Strict — purely functional balanced BST map
-- import qualified Data.Map.Strict as Map
--
-- let m = Map.fromList [("alice", 30), ("bob", 25), ("carol", 28)]
-- Map.lookup "alice" m          -- Just 30
-- Map.member "dave" m           -- False
-- Map.insert "dave" 35 m        -- new map with dave
-- Map.delete "bob" m            -- map without bob
-- Map.map (+1) m                -- increment all values
-- Map.filter (> 27) m           -- only values > 27
-- Map.unionWith (+) m1 m2       -- merge with conflict resolution

-- TODO 2: Data.Set — purely functional balanced BST set
-- import qualified Data.Set as Set
--
-- let s1 = Set.fromList [1, 2, 3, 4, 5]
-- let s2 = Set.fromList [3, 4, 5, 6, 7]
-- Set.intersection s1 s2        -- {3,4,5}
-- Set.union s1 s2               -- {1..7}
-- Set.difference s1 s2          -- {1,2}
-- Set.member 3 s1               -- True
-- Set.toAscList s1              -- [1,2,3,4,5] sorted

-- TODO 3: Data.Sequence — O(log n) access and update, efficient split/join
-- import qualified Data.Sequence as Seq
--
-- let s = Seq.fromList [1..5]
-- Seq.index s 2                 -- 3 (0-indexed)
-- Seq.update 2 99 s             -- [1,2,99,4,5]
-- Seq.insertAt 1 10 s           -- [1,10,2,3,4,5]
-- fst (Seq.splitAt 3 s)         -- [1,2,3]

-- TODO 4: Data.IntMap — specialized Map for Int keys (faster)
-- import qualified Data.IntMap.Strict as IntMap
-- Useful for: sparse arrays, frequency tables, adjacency lists for graphs

-- TODO 5: Custom BST — implement from scratch
-- data BST a = Empty | BSTNode a (BST a) (BST a)
--
-- insert :: Ord a => a -> BST a -> BST a
-- insert x Empty = BSTNode x Empty Empty
-- insert x (BSTNode v l r)
--   | x < v    = BSTNode v (insert x l) r
--   | x > v    = BSTNode v l (insert x r)
--   | otherwise = BSTNode v l r
--
-- toList :: BST a -> [a]
-- toList Empty = []
-- toList (BSTNode v l r) = toList l ++ [v] ++ toList r

-- TODO 6: Priority Queue using Data.Set
-- newtype PQueue a = PQueue (Set.Set (Int, a))  -- (priority, value)
--
-- push :: Int -> a -> PQueue a -> PQueue a
-- push p v (PQueue s) = PQueue (Set.insert (p, v) s)  -- assumes unique priorities
--
-- pop :: PQueue a -> Maybe (a, PQueue a)
-- pop (PQueue s)
--   | Set.null s = Nothing
--   | otherwise  = let (_, v) = Set.findMin s in Just (v, PQueue (Set.deleteMin s))

-- TODO 7: HashMap (from unordered-containers)
-- import qualified Data.HashMap.Strict as HashMap
-- Faster than Data.Map for non-ordered access (uses hashing)
-- API mirrors Data.Map: insert, lookup, member, delete, map, filter, unionWith

-- TODO 8: IORef — mutable reference in IO
-- import Data.IORef
-- main :: IO ()
-- main = do
--   ref <- newIORef (0 :: Int)      -- create mutable ref
--   modifyIORef' ref (+1)           -- strict modify
--   modifyIORef' ref (+1)
--   val <- readIORef ref
--   print val                        -- 2
