
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Random;
//import java.util.concurrent.TimeUnit;

public class Visualizer extends JFrame {
    ArrayList<Integer> nums = new ArrayList<Integer>();
    int i = 0;
    int j = 1;
    int k = 0;
    int n1;
    int n2;
    int key;
    ArrayList<Integer> L = new ArrayList<Integer>();
    ArrayList<Integer> R = new ArrayList<Integer>();

    class MyGraphics extends JPanel {
        private static final long serialVersionUID = 1L;

        @Override
        public Dimension getMinimumSize() {
            return new Dimension(1000, 300);
        }

        @Override
        public Dimension getPreferredSize() {
            return new Dimension(1000, 300); // appropriate constants
        }

        @Override
        public Dimension getMaximumSize() {
            return new Dimension(1000, 300);
        }

        @Override
        public void paintComponent(Graphics g) {
            super.paintComponent(g);
            int max = Collections.max(nums);
            for (int i = 0; i < nums.size(); i++)
                g.drawRect((int) (i * 1000 / nums.size()), (int) (300 - nums.get(i) * 300 / max),
                        (int) (1000 / nums.size()), (int) (nums.get(i) * 300 / max));
            // System.out.println(nums);
        }

        public void bubbleSort() {
            i = 0;
            j = 1;
            Timer timer = new Timer(10, new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {

                    if (nums.get(j) > nums.get(i)) {
                        int temp = nums.get(i);
                        nums.set(i, nums.get(j));
                        nums.set(j, temp);
                        repaint();
                    }
                    j++;
                    if (j >= nums.size()) {
                        i++;
                        j = i + 1;

                        // System.out.println(i + " " + j);
                        if (j >= nums.size() || i >= nums.size())
                            ((Timer) e.getSource()).stop();

                    }
                }
            });
            timer.setRepeats(true);
            timer.start();

        }

        public void insertionSort() {
            i = 1;
            key = nums.get(i);
            j = i - 1;
            Timer timer = new Timer(10, new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    if (j >= 0 && nums.get(j) < key) {
                        nums.set(j + 1, nums.get(j));
                        repaint();
                        j = j - 1;
                    } else {
                        nums.set(j + 1, key);
                        repaint();
                        i++;
                        j = i - 1;
                        if (i >= nums.size())
                            ((Timer) e.getSource()).stop();
                        else
                            key = nums.get(i);
                    }

                }
            });
            timer.setRepeats(true);
            timer.start();
        }

        public void merge(int l, int m, int r) {

            n1 = m - l + 1;
            n2 = r - m;
            L.clear();
            R.clear();
            // Copy data to temp arrays
            for (int x = 0; x < n1; ++x)
                L.add(nums.get(l + x));
            for (int x = 0; x < n2; ++x)
                R.add(nums.get(m + 1 + x));

            i = 0;
            j = 0;
            k = l;
            System.out.println("start");
            Timer timer = new Timer(10, null);
            timer.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    System.out.println(k);
                    if (i < n1 && j < n2) {
                        if (L.get(i) >= R.get(j)) {
                            nums.set(k, L.get(i));
                            i++;
                        } else {
                            nums.set(k, R.get(j));
                            j++;
                        }
                        k++;
                    } else if (i < n1) {
                        nums.set(k, L.get(i));
                        i++;
                        k++;
                    } else if (j < n2) {
                        nums.set(k, R.get(j));
                        j++;
                        k++;
                    } else
                        ((Timer) e.getSource()).stop();
                    repaint();
                }
            });
            timer.setRepeats(true);
            timer.start();

        }

        public void mergeSort(int l, int r) {

            if (l < r) {

                // Find the middle point
                int m = l + (r - l) / 2;
                // SwingUtilities.invokeLater(
                //         new Runnable() {
                //             public void run() {
                //                 mergeSort(l, m);
                //                 mergeSort(m + 1, r);
                //             }
                //         });
                // Merge the sorted halves
                //System.out.println(l + " " + " " + m + " " + r);
                merge(l, m, r);
            }

        }
    }

    public void scramble(int range) {
        Random random = new Random();
        nums.clear();
        ArrayList<Integer> temp = new ArrayList<Integer>();
        for (int i = 0; i <= range; i++)
            temp.add(i + 1);
        int size = temp.size();
        for (int i = 0; i < size; i++) {
            int idx = random.nextInt(temp.size());
            nums.add(temp.get(idx));
            temp.remove(idx);
        }
    }

    public void draw(Graphics g, MyGraphics p) {
        p.paintComponents(g);
    }

    public void createGUI() {
        scramble(20);
        JFrame main = new JFrame("Sorting Visualizer");
        main.setSize(1000, 600);
        main.setLayout(null);
        main.setVisible(true);
        Image icon = Toolkit.getDefaultToolkit().getImage("penisforeskinicon.JPG");
        main.setIconImage(icon);

        JPanel display = new JPanel();
        display.setBounds(0, 300, 1000, 300);
        display.setSize(new Dimension(1000, 300));
        MyGraphics p = new MyGraphics();
        p.setSize(1000, 300);
        p.setBounds(0, 300, 1000, 300);
        main.add(p);

        // draw(g,p);

        // bubble sort button
        Button button = new Button("Bubble Sort");
        button.setBounds(150, 130, 100, 30);
        main.add(button);
        button.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                p.bubbleSort();
            }
        });

        // merge sort button
        Button button2 = new Button("Merge Sort");
        button2.setBounds(1000 / 2 - 50, 130, 100, 30);
        main.add(button2);
        button2.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                SwingUtilities.invokeLater(
                        new Runnable() {
                            public void run() {
                                SwingUtilities.invokeLater(
                                        new Runnable() {
                                            public void run() {
                                                p.mergeSort(0, nums.size() - 1);
                                            }
                                        });
                            }
                        });

            }
        });

        // insert sort button
        Button button3 = new Button("Insertion Sort");
        button3.setBounds(1000 - 250, 130, 100, 30);
        main.add(button3);
        button3.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                p.insertionSort();
            }
        });
        // input range
        // TextField range = new TextField();
        // range.setBounds(150, 180, 100, 30);
        // main.add(range);

        // scramble button
        Button button4 = new Button("Scramble");
        button4.setBounds(150, 180, 100, 30);
        main.add(button4);
        button4.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                scramble(20);
                p.repaint();
            }
        });
        main.addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent e) {
                System.exit(0);
            }
        });
    }

    public static void main(String[] args) {
        Visualizer GUI = new Visualizer();
        GUI.createGUI();
    }
}