%include	/usr/lib/rpm/macros.python

%define		zope_subname	CMFSin

Summary:	CMFSin is a Zope product - This is a simple syndication client for CMF
Summary(pl):	CMFSin jest dodatkiem do Zope - Prosty klient "korporacyjny" dla CMF
Name:		Zope-%{zope_subname}
Version:	0.6.1
Release:	1
License:	GNU
Group:		Development/Tools
Source0:	http://switch.dl.sourceforge.net/sourceforge/collective/%{zope_subname}.tar.gz
# Source0-md5:	a50ab5b9c13526a6a52397d556b09e84
URL:		http://sourceforge.net/projects/collective
%pyrequires_eq	python-modules
Requires:	Zope
Requires:	CMF
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	product_dir	/usr/lib/zope/Products

%description
This is a simple syndication client for CMF. It uses rssparser and
shares many things in common with CMFNewsFeed but has a different
model for handling channels. It is designed to map _n_ channels or
feeds to sets of composite virtual channels which can then be called
in in a timely fashion.

%description -l pl
CMFSin jest prostym klientem "korporacyjnym" dla CMF. Umo¿liwia
parsowanie rss i posiada wiele mo¿liwosæi jakie daje CMFNewsFeed lecz
ró¿ni siê innym modelem obs³ugi kana³ów. Jest stworzony dla ob³ugi
kana³ów typu _n_ lub wirtualnych kana³ów tworzonych o okre¶lonej
porze.

%prep
%setup -q -c %{zope_subname}-%{version}

%build
cd %{zope_subname}
rm -fR `find . -type d -name CVS`
mv -f README.txt docs/

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{product_dir}
cp -af * $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

rm -rf $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}/debian

%py_comp $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}
%py_ocomp $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;
rm -rf $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}/docs


%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%preun

%postun
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%files
%defattr(644,root,root,755)
%doc %{zope_subname}/docs/*
%{product_dir}/%{zope_subname}
